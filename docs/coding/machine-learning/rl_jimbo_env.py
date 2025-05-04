# %% [markdown]
# # RL Lab 5: Jimbo Game
#
# 小丑牌问题环境搭建
#
# ## 简介
#
# 网格迷宫问题是一类常见的序列决策问题，其状态转移和奖励函数都较为简单，仅使用动态规划方法就可以求解出最优策略。此处，我们需要引入一个更复杂的强化学习环境，以便于我们在后续的实验中使用。
#
# ## 目标
#
# 在`BaseJimboEnvironment`类的基础上实现一个`JimboEnvironment`。该环境需要实现：
#
# * 定义环境状态。
# * 随机化地洗牌、发牌。
# * 计算当前状态的奖励和倍率。其中奖励为所有5张牌的点数之和（A计为11分），倍率为牌型的倍率。具体的倍率如下：
#
# | 牌型 | 描述 | 倍率 |
# | ---- | ---- | ---- |
# | 皇家同花顺 | 相同花色的10、J、Q、K、A | +10 |
# | 同花顺 | 相同花色的顺子 | +9 |
# | 四条 | 有 4 张点数相同的牌 | +8 |
# | 葫芦 | 有 3 张牌点数相同，且另外两张牌点数也相同 | +7 |
# | 同花 | 花色相同但点数不连续的 5 张牌 | +6 |
# | 顺子 | 点数连续的 5 张牌 | +5 |
# | 三条 | 有 3 张点数相同的牌 | +4 |
# | 两对 | 有 2 个对子 | +3 |
# | 对子 | 有 2 张点数相同的牌 | +2 |
# | 高牌 | 凑不出以上任何牌型 | +1 |
#
# ## 拓展
#
# * 如何加快环境的响应速度？

# %%
from collections import Counter
import enum
import dataclasses
import abc
import itertools
import random
import functools
import numpy as np

from typing import TypeVar, Generic, Tuple, Set, List

StateType = TypeVar('StateType')
ActionType = TypeVar('ActionType')

if __name__ == '__main__':
    # seed = random.randint(0, 10000)
    seed = 7218
    print(f"Seed: {seed}")
    random.seed(seed)

# %%


class Suit(enum.IntEnum):
    '''
    Enum for the 4 suits
    '''
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3


@dataclasses.dataclass(frozen=True)
class Card:
    '''
    Class for a card
    '''
    suit: Suit
    rank: int

    @property
    def score(self) -> int:
        if self.rank == 1:
            return 11
        return self.rank

    @property
    def index(self) -> int:
        return self.suit.value * 13 + self.rank

    def __str__(self):
        rank = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }.get(self.rank, str(self.rank))
        suits = {
            Suit.HEARTS: '♥',
            Suit.DIAMONDS: '♦',
            Suit.CLUBS: '♣',
            Suit.SPADES: '♠'
        }.get(self.suit, '?')
        return f'{rank}{suits}'


ALL_CARDS = {
    Card(suit, rank)
    for suit, rank in itertools.product(Suit, range(1, 14))
}


def draw(n: int = 1, exclude: Set[Card] | None = None) -> List[Card]:
    if exclude is None:
        exclude = set()
    if n > len(ALL_CARDS) - len(exclude):
        raise ValueError(f'Cannot draw {n} cards from {len(ALL_CARDS) - len(exclude)} remaining cards')
    available_cards = list(ALL_CARDS - exclude)
    drawn_cards = random.sample(available_cards, n)
    return drawn_cards


class BaseJimboEnvironment(abc.ABC, Generic[StateType, ActionType]):
    def __init__(self):
        pass

    @property
    @abc.abstractmethod
    def starting_state(self) -> StateType:
        '''
        The starting state of the environment
        '''
        pass

    @abc.abstractmethod
    def state_transition(self, state: StateType, action: ActionType) -> Tuple[StateType, float]:
        '''
        Given a state and an action, sample a next state and a reward
        '''
        pass

    @abc.abstractmethod
    def evaluate_state(self, state: StateType) -> float:
        '''
        Evaluate the value of a state
        '''
        pass

# %% [markdown]
# 首先定义扑克牌，其次在此基础上定义状态。


# %%


@dataclasses.dataclass(frozen=True)
class JimboState():
    hold: Tuple[Card, ...]
    discard: Tuple[Card, ...]
    round: int

    def __str__(self):
        return ' '.join([str(card) for card in self.hold])

    @property
    def points(self) -> int:
        return sum(card.score for card in self.hold)

    @property
    def ratio(self) -> int:
        return self._ratio(self.hold)

    @property
    @functools.lru_cache(maxsize=None)
    def score(self) -> int:
        return self.points * self.ratio

    @staticmethod
    @functools.lru_cache(maxsize=None)
    def _ratio(hold: Tuple[Card, ...]) -> int:
        '''
        Evaluate the value of a state

        牌型	描述	倍率
        皇家同花顺	相同花色的10、J、Q、K、A	+10
        同花顺	相同花色的顺子	+9
        四条	有 4 张点数相同的牌	+8
        葫芦	有 3 张牌点数相同，且另外两张牌点数也相同	+7
        同花	花色相同但点数不连续的 5 张牌	+6
        顺子	点数连续的 5 张牌	+5
        三条	有 3 张点数相同的牌	+4
        两对	有 2 个对子	+3
        对子	有 2 张点数相同的牌	+2
        高牌	凑不出以上任何牌型	+1
        '''
        rank = sorted([card.rank for card in hold])
        rank_set = set(rank)
        rank_counter = Counter(rank)
        suit = [card.suit for card in hold]
        suit_set = set(suit)

        # Royal Flush
        if len(suit_set) == 1 and {10, 11, 12, 13, 1}.issubset(rank_set):
            return 10
        # Straight Flush
        if len(suit_set) == 1 and \
                len(rank_set) == 5 and \
                max(rank) - min(rank) == 4:
            return 9
        # Four of a Kind
        if max(rank_counter.values()) == 4:
            return 8
        # Full House
        if len(rank_set) == 2 and \
                max(rank_counter.values()) == 3:
            return 7
        # Flush
        if len(suit_set) == 1:
            return 6
        # Straight
        if len(rank_set) == 5 and max(rank) - min(rank) == 4:
            return 5
        # Three of a Kind
        if max(rank_counter.values()) == 3:
            return 4
        # Two Pair
        if len(rank_set) == 3 and \
                max(rank_counter.values()) == 2:
            return 3
        # One Pair
        if max(rank_counter.values()) == 2:
            return 2
        # High Card
        return 1

    @property
    def end(self) -> bool:
        '''
        Whether the game is over
        '''
        return self.round == 2

# %% [markdown]
# 在每一轮中，智能体选择是否弃牌，弃牌后重新发牌，所有轮次结束后，智能体按照牌型获得奖励。

# %%


@dataclasses.dataclass(frozen=True)
class JimboAction():
    discard: Tuple[bool, ...]

    @property
    @functools.lru_cache(maxsize=None)
    def index(self) -> int:
        '''
        The index of the action
        '''
        return sum([2 ** i for i, discard in enumerate(self.discard) if discard])

    @classmethod
    @functools.lru_cache(maxsize=None)
    def from_index(cls, index: int) -> 'JimboAction':
        '''
        Create an action from an index
        '''
        discard = []
        for i in range(5):
            discard.append(bool(index % 2))
            index //= 2
        return cls(tuple(discard))

# %% [markdown]
# 在此基础上，定义Jimbo环境。

# %%


class JimboEnvironment(BaseJimboEnvironment[JimboState, JimboAction]):
    def __init__(self):
        super().__init__()

    @property
    def starting_state(self) -> JimboState:
        return JimboState(hold=tuple(draw(5)), discard=(), round=0)

    def state_transition(self, state: JimboState, action: JimboAction) -> Tuple[JimboState, float]:
        '''
        Given a state and an action, sample a next state and a reward
        '''
        if state is None:
            return None, 0.0

        current_hold = list(state.hold)
        past_discard = list(state.discard)

        new_card = draw(5, exclude=set(state.hold) | set(state.discard))
        for idx, discard in enumerate(action.discard):
            if discard:
                past_discard.append(current_hold[idx])
                current_hold[idx] = new_card[idx]
        new_state = JimboState(
            hold=tuple(current_hold),
            discard=tuple(past_discard),
            round=state.round + 1
        )
        if new_state.end:
            reward = self.evaluate_state(new_state)
            return new_state, reward
        else:
            return new_state, 0

    def evaluate_state(self, state: JimboState) -> float:
        return state.score


# %%
if __name__ == '__main__':
    env = JimboEnvironment()
    state = env.starting_state
    print(state)
    action = JimboAction(discard=(True, False, False, False, True))
    state, _ = env.state_transition(state, action)
    action = JimboAction(discard=(True, False, False, False, True))
    next_state, reward = env.state_transition(state, action)
    assert next_state is not None
    print(next_state)
    print(reward)
    print(next_state.ratio)

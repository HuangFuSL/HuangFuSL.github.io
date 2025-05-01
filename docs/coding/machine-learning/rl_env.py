# %% [markdown]
# # RL Lab 1: Environment
#
# 网格迷宫问题环境搭建
#
# ## 简介
#
# 网格迷宫问题是一类常见的序列决策问题。智能体在网格迷宫中移动，其目标是移动到迷宫中的目标位置。除了目标外，迷宫中存在阻碍智能体移动的墙壁、为智能体提供额外加分的奖励点、以及智能体需要避免经过的陷阱。网格迷宫问题的特点是有限状态和离散动作，假设智能体能够观测到迷宫的全貌。
#
# ## 目标
#
# 在`BaseGridEnvironment`类的基础上实现一个二维的网格迷宫环境`GridWorldEnvironment`。该环境需要实现：
#
# * 随机地初始化迷宫，迷宫中随机地分布着墙壁。
# * 定义状态和状态索引，定义动作和动作索引
# * 为智能体的移动设计奖励函数
#   * 奖励函数可以在智能体采取特定状态，或到达特定位置时触发。
# * 设计状态转移函数
#
# ### 扩展
#
# 如何生成更真实的随机障碍，和保证生成的迷宫一定有解？

# %% [markdown]
# ## 代码实现
#
# 导入必要的包

# %%
import enum
import dataclasses
import abc
import torch
import random
from matplotlib import pyplot as plt
import functools

from typing import TypeVar, overload, Generic, Iterable, Tuple

StateType = TypeVar('StateType')
ActionType = TypeVar('ActionType')

# %%


class BaseGridEnvironment(abc.ABC, Generic[StateType, ActionType]):
    def __init__(
        self, ncols: int, nrows: int,
        branch_ratio: float = 0.1, device: str = 'cpu'
    ):
        self.ncols = ncols
        self.nrows = nrows
        self.branch_ratio = branch_ratio

        self.grid = torch.zeros((nrows, ncols), dtype=torch.long)
        self.generate_grid()
        self.device = device

        states = [*enumerate(set(self.all_states()))]
        self.states = {
            idx: state for idx, state in states
        } | {
            state: idx for idx, state in states
        }

        actions = [*enumerate(set(self.all_actions()))]
        self.actions = {
            idx: action for idx, action in actions
        } | {
            action: idx for idx, action in actions
        }

    @property
    def num_states(self) -> int:
        return len(self.states) // 2

    @property
    def num_actions(self) -> int:
        return len(self.actions) // 2

    @property
    @abc.abstractmethod
    def starting_state(self) -> StateType:
        pass

    @property
    @abc.abstractmethod
    def ending_state(self) -> StateType:
        pass

    @abc.abstractmethod
    def generate_grid(self) -> None:
        pass

    @abc.abstractmethod
    def all_states(self) -> Iterable[StateType]:
        pass

    @abc.abstractmethod
    def all_actions(self) -> Iterable[ActionType]:
        pass

    @overload
    def get_state(self, state: int) -> StateType:
        pass

    @overload
    def get_state(self, state: StateType) -> int:
        pass

    def get_state(self, state: StateType | int) -> StateType | int:
        return self.states[state]

    @overload
    def get_action(self, action: int) -> ActionType:
        pass

    @overload
    def get_action(self, action: ActionType) -> int:
        pass

    def get_action(self, action: ActionType | int) -> ActionType | int:
        return self.actions[action]

    @overload
    def get_state_action(self, obj: Tuple[StateType, ActionType]) -> int:
        pass

    @overload
    def get_state_action(self, obj: int) -> Tuple[StateType, ActionType]:
        pass

    def get_state_action(
        self, obj: Tuple[StateType, ActionType] | int
    ) -> Tuple[StateType, ActionType] | int:
        if isinstance(obj, tuple):
            state, action = obj
            return self.get_state(state) * self.num_actions + self.get_action(action)
        else:
            idx = obj
            state_idx = idx // self.num_actions
            action_idx = idx % self.num_actions
            return self.get_state(state_idx), self.get_action(action_idx)

    @abc.abstractmethod
    def state_transition(self, state: StateType, action: ActionType) -> Iterable[Tuple[StateType, float]]:
        '''
        Given a state and an action, return a list of tuples (next_state, probability).
        '''
        pass

    @property
    @functools.lru_cache()
    def state_transition_np(self) -> torch.Tensor:
        '''
        Build a state transition matrix, by calling `state_transition()`
        The state transition matrix is a 2D sparse tensor of shape
        (num_states * num_actions, num_states). The value at (s * num_actions + a, s') is the
        probability of transitioning from state s to state s' given action a.
        '''
        row_indices = []
        col_indices = []
        values = []

        for s in range(self.num_states):
            state = self.get_state(s)
            for a in range(self.num_actions):
                action = self.get_action(a)
                index = s * self.num_actions + a

                for next_state, prob in self.state_transition(state, action):
                    next_state_idx = self.get_state(next_state)
                    row_indices.append(index)
                    col_indices.append(next_state_idx)
                    values.append(prob)

        indices = torch.tensor([row_indices, col_indices], dtype=torch.long)
        values = torch.tensor(values, dtype=torch.float32)
        shape = (self.num_states * self.num_actions, self.num_states)

        return torch.sparse_coo_tensor(indices, values, size=shape, device=self.device)

    @abc.abstractmethod
    def step_reward(
        self, state: StateType, action: ActionType, next_state: StateType
    ) -> float:
        '''
        Calculate the reward for taking an action in a state.
        '''
        pass

    @property
    @functools.lru_cache()
    def step_reward_np(self) -> torch.Tensor:
        '''
        Build a reward matrix, by calling `step_reward()`.
        The reward matrix is a 2D sparse tensor of shape
        (num_states * num_actions, num_states). The value at (s * num_actions + a, s') is the
        reward of transitioning from state s to state s' given action a.
        '''
        row_indices = []
        col_indices = []
        values = []

        for s in range(self.num_states):
            state = self.get_state(s)
            for a in range(self.num_actions):
                action = self.get_action(a)
                index = s * self.num_actions + a
                for next_state, _ in self.state_transition(state, action):
                    next_state_val = self.get_state(next_state)
                    reward = self.step_reward(state, action, next_state)

                    if reward != 0:  # You can optimize by ignoring zero rewards if needed
                        row_indices.append(index)
                        col_indices.append(next_state_val)
                        values.append(reward)

        indices = torch.tensor([row_indices, col_indices], dtype=torch.long)
        values = torch.tensor(values, dtype=torch.float32)
        shape = (self.num_states * self.num_actions, self.num_states)

        return torch.sparse_coo_tensor(indices, values, size=shape, device=self.device)

# %% [markdown]
# ### 状态
#
# 状态为智能体在网格中的位置。


# %%


@dataclasses.dataclass(frozen=True)
class State():
    row: int
    col: int

    def __iter__(self):
        return iter([self.row, self.col])

    def __add__(self, other: 'Action'):
        return State(self.row + other.value[0], self.col + other.value[1])

# %% [markdown]
# ### 动作
#
# 智能体可以向上、下、左、右四个方向移动。


# %%


class Action(enum.Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

# %% [markdown]
# ### 环境
#
# 环境需要实现动作空间、状态空间、奖励函数和状态转移函数。

# %%


class GridEnvironment(BaseGridEnvironment[State, Action]):
    def __init__(self, ncols: int, nrows: int, wall_ratio: float = 0.1, device: str = 'cpu'):
        if not (ncols % 2 and nrows % 2):
            raise ValueError('Number of columns and rows should be odd.')
        super().__init__(ncols, nrows, wall_ratio, device)

    @property
    def starting_state(self) -> State:
        return State(1, 1)

    @property
    def ending_state(self) -> State:
        return State(self.nrows - 2, self.ncols - 2)

    def all_states(self):
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.grid[row, col] == 0:
                    yield State(row, col)

    def all_actions(self):
        for action in Action:
            yield action

    def state_transition(self, state: State, action: Action) -> Iterable[Tuple[State, float]]:
        if state == self.ending_state:
            # Terminal state
            yield state, 1.0
            return

        move_row, move_col = action.value
        next_row, next_col = state.row + move_row, state.col + move_col
        if 0 <= next_row < self.nrows and 0 <= next_col < self.ncols:
            if self.grid[next_row, next_col] == 0:
                yield State(next_row, next_col), 1.0
            else:
                # hit a wall
                yield state, 1.0
        else:
            # out of bounds
            yield state, 1.0

    def step_reward(self, state: State, action: Action, next_state: State) -> float:
        if next_state == self.ending_state:
            if state == next_state:
                return 0.0
            else:
                return 50.0
        elif state == next_state:
            return -1  # hit a wall

        return -0.1  # Step cost

    def generate_grid(self):
        sy, sx = self.starting_state
        ey, ex = self.ending_state
        grid = torch.ones((self.nrows, self.ncols), dtype=torch.long)

        visited = set()
        stack = []

        def carve_from(cell: Tuple[int, int]):
            visited.add(cell)
            stack.append(cell)
            grid[cell] = 0

            while stack:
                cy, cx = stack[-1]
                neighbors = []
                # four directions, step two cells
                for dy, dx in ((0, 2), (0, -2), (2, 0), (-2, 0)):
                    ny, nx = cy + dy, cx + dx
                    # remain inside inner area
                    if 1 <= ny < self.nrows - 1 and 1 <= nx < self.ncols - 1 and (ny, nx) not in visited:
                        neighbors.append((ny, nx))

                if neighbors:
                    ny, nx = random.choice(neighbors)
                    # remove wall between current and neighbor
                    wy, wx = (cy + ny) // 2, (cx + nx) // 2
                    grid[wy, wx] = 0
                    grid[ny, nx] = 0
                    visited.add((ny, nx))
                    stack.append((ny, nx))
                else:
                    stack.pop()

        # Carve primary tree from start
        carve_from((sy, sx))

        # Add extra branches (loops) to introduce complexity
        if self.branch_ratio > 0:
            for y in range(1, self.nrows - 1, 2):
                for x in range(1, self.ncols - 1, 2):
                    for dy, dx in ((0, 2), (2, 0)):
                        ny, nx = y + dy, x + dx
                        wy, wx = y + dy // 2, x + dx // 2
                        if ny < self.nrows - 1 and nx < self.ncols - 1:
                            if grid[y, x] == 0 and grid[ny, nx] == 0 and grid[wy, wx] == 1:
                                if random.random() < self.branch_ratio:
                                    grid[wy, wx] = 0

        # Ensure start and end positions are open
        grid[sy, sx] = 0
        grid[ey, ex] = 0

        self.grid = grid

# %% [markdown]
# ### 运行测试
#
# 测试迷宫生成


# %%
if __name__ == '__main__':
    env = GridEnvironment(25, 25, wall_ratio=0.07)
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))

    grid_to_show = 2 * env.grid.clone().cpu().numpy()
    grid_to_show[*env.starting_state] = 1
    grid_to_show[*env.ending_state] = 1

    ax.imshow(grid_to_show, cmap='gray', interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect(env.ncols / env.nrows)

    plt.show()

# %% [markdown]
# 测试状态数、动作数

# %%
if __name__ == '__main__':
    print(f'Environment have {env.num_states} states')
    print(f'Environment have {env.num_actions} states')

# %% [markdown]
# 测试状态转移矩阵和奖励矩阵

# %%
if __name__ == '__main__':
    def get_size(x): return x.numel() * x.element_size()
    print(f'State transition matrix takes {get_size(env.state_transition_np) / (2 ** 20):.2f} MB')
    print(f'Reward matrix takes {get_size(env.state_transition_np) / (2 ** 20):.2f} MB')

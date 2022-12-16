window.MathJax = {
    tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true
    },
    chtml: { scale: 0.8 },
    svg: { scale: 0.8 },
    options: {
        ignoreHtmlClass: '.*|',
        processHtmlClass: 'arithmatex'
    }
};

document$.subscribe(() => {
    MathJax.typesetPromise();
});

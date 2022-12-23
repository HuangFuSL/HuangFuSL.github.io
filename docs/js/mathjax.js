window.MathJax = {
    tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true,
        packages: { '[+]': ['boldsymbol'] }
    },
    chtml: { scale: 0.8 },
    svg: { scale: 0.8 },
    options: {
        ignoreHtmlClass: '.*|',
        processHtmlClass: 'arithmatex'
    },
    loader: { load: ['[tex]/boldsymbol'] },
};

document$.subscribe(() => {
    MathJax.typesetPromise();
});

window.MathJax = {
    tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true,
        packages: { '[+]': ['boldsymbol', 'bbox'] }
    },
    chtml: { scale: 0.8 },
    svg: { scale: 0.8 },
    options: {
        ignoreHtmlClass: '.*|',
        processHtmlClass: 'arithmatex'
    },
    loader: { load: ['[tex]/boldsymbol', '[tex]/bbox'] }
};

document$.subscribe(() => {
    MathJax.typesetPromise();
});

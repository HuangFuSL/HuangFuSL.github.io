// Using the document$ observable from mkdocs-material to get notified of page "reload" also if using `navigation.instant` (SSA)
document$.subscribe(function () {
    // First check if the page contains a notebook-related class
    if (document.querySelector('.jp-Notebook')) {
        // Remove table of contents
        document.querySelector('.md-sidebar--secondary').remove();
    }
});

(function () {
  var path = window.location.pathname;
  if (path === '/' || path.endsWith('/index.html')) {
    var style = document.createElement('style');
    style.textContent = '.md-sidebar--secondary { display: none !important; }';
    document.head.appendChild(style);
  }
})();

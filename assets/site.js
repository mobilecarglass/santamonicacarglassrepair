(function () {
  'use strict';

  function initMobileMenu() {
    var button = document.querySelector('.menu');
    var nav = document.querySelector('.links');
    var backdrop = document.querySelector('.backdrop');

    if (!button || !nav) return;

    function closeMenu() {
      nav.classList.remove('open');
      if (backdrop) backdrop.classList.remove('show');
      document.body.classList.remove('menu-open');
      button.setAttribute('aria-expanded', 'false');
      button.setAttribute('aria-label', 'Open navigation');
      nav.querySelectorAll('.drop.open').forEach(function (item) {
        item.classList.remove('open');
      });
    }

    function openMenu() {
      nav.classList.add('open');
      if (backdrop) backdrop.classList.add('show');
      document.body.classList.add('menu-open');
      button.setAttribute('aria-expanded', 'true');
      button.setAttribute('aria-label', 'Close navigation');
    }

    button.addEventListener('click', function (event) {
      event.preventDefault();
      event.stopPropagation();
      if (nav.classList.contains('open')) closeMenu();
      else openMenu();
    });

    if (backdrop) {
      backdrop.addEventListener('click', function (event) {
        event.preventDefault();
        closeMenu();
      });
    }

    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        closeMenu();
      });
    });

    nav.querySelectorAll('.dropbtn').forEach(function (dropButton) {
      dropButton.addEventListener('click', function (event) {
        event.preventDefault();
        event.stopPropagation();
        dropButton.parentElement.classList.toggle('open');
      });
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') closeMenu();
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 780) closeMenu();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileMenu);
  } else {
    initMobileMenu();
  }
})();

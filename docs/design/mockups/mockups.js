// SPDX-License-Identifier: MPL-2.0
// Mockup helpers only: the theme switch and the first-run steps. Nothing here
// is product code, and every page reads correctly with scripting off.
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.add("js");

  function readTheme() {
    try { return window.localStorage.getItem("brumel-mockup-theme") || "system"; } catch (e) { return "system"; }
  }
  function applyTheme(value) {
    if (value === "system") { root.removeAttribute("data-theme"); } else { root.setAttribute("data-theme", value); }
    try { window.localStorage.setItem("brumel-mockup-theme", value); } catch (e) { /* storage unavailable */ }
  }

  var params = new URLSearchParams(window.location.search);
  var initial = params.get("theme") || readTheme();
  applyTheme(initial);
  document.querySelectorAll('input[name="mock-theme"]').forEach(function (input) {
    input.checked = input.value === initial;
    input.addEventListener("change", function () { if (input.checked) { applyTheme(input.value); } });
  });

  // Keep the current item of a scrolling nav strip in view on narrow screens.
  function centreCurrentNavItem() {
    document.querySelectorAll(".webui__nav").forEach(function (nav) {
      var current = nav.querySelector('[aria-current="page"]');
      if (current && nav.scrollWidth > nav.clientWidth) {
        nav.scrollLeft = current.offsetLeft - (nav.clientWidth - current.offsetWidth) / 2;
      }
    });
  }
  centreCurrentNavItem();
  window.addEventListener("load", centreCurrentNavItem);
  window.addEventListener("resize", centreCurrentNavItem);

  // First run: show one step at a time; without scripting all steps stay visible.
  var steps = Array.prototype.slice.call(document.querySelectorAll("[data-step]"));
  var markers = Array.prototype.slice.call(document.querySelectorAll("[data-step-marker]"));
  function show(index) {
    steps.forEach(function (step, i) {
      if (i === index) { step.setAttribute("data-active", ""); } else { step.removeAttribute("data-active"); }
    });
    markers.forEach(function (marker, i) {
      if (i === index) { marker.setAttribute("aria-current", "step"); } else { marker.removeAttribute("aria-current"); }
    });
    var heading = steps[index] && steps[index].querySelector("h2");
    if (heading && document.activeElement && document.activeElement.closest("[data-step]")) {
      heading.setAttribute("tabindex", "-1");
      heading.focus({ preventScroll: true });
    }
  }
  if (steps.length) {
    show(Number(params.get("step") || 0));
    document.querySelectorAll("[data-goto]").forEach(function (button) {
      button.addEventListener("click", function () { show(Number(button.getAttribute("data-goto"))); });
    });
  }
})();

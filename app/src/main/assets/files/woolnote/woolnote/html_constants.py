# TODO: docstring for the file

# constants for HTML contents
#############################

HTML_VIEWPORT_META = """<meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, user-scalable=no, user-scalable=0"/>"""

# the class uk-button ignores span's font size but when uikit is not loaded (need to use uk-button uk-button-large), the span at least still conveys the info that this should be big
HTML_SPAN_STYLE_BIG = "style=\"font-size:20pt; \""

HTML_NOTE_LINK_WITH_PREVIEW = """
<a href="/woolnote?{request_params}" style="text-decoration: none"  ><div>{sanitized_task_name}{sanitized_due_date}<br>
<small><small>{sanitized_task_folder}; {sanitized_task_tags}</small></small><br>
<small>{sanitized_body_snippet}</small></div></a><hr>
""".strip()

HTML_JS_EVENT_TEXTAREA_RESIZE = "if (document.getElementById('TaTb').scrollHeight > document.getElementById('TaTb').clientHeight) {document.getElementById('TaTb').style.height = (document.getElementById('TaTb').scrollHeight + 10) + 'px'; } "

HTML_ELEM_ATTR_JS_EVENTS_TEXTAREA_RESIZE = """ onclick="{js_event_textarea}" oninput="{js_event_textarea}" onfocus="{js_event_textarea}" onmouseover="{js_event_textarea}" onscroll="{js_event_textarea}" onmousemove="{js_event_textarea}" onmouseenter="{js_event_textarea}" onload="{js_event_textarea}" onpageshow="{js_event_textarea}" onwheel="{js_event_textarea}" ontouchstart="{js_event_textarea}" ontouchmove="{js_event_textarea}"  """.format(
    js_event_textarea=HTML_JS_EVENT_TEXTAREA_RESIZE)

HTML_UIKIT_LINK_REL_ONLINE = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/uikit/2.15.0/css/uikit.gradient.min.css">"""
HTML_UIKIT_2_27_1_LINK_REL_LOCAL = """<link rel="stylesheet" href="../uikit-2.27.1.gradient-customized.css.v5.css">"""  # increasing number because of caching&development

# with edits (comments in css):
# the "\" characters had to be escaped in the css (due to Python evaluating \somecode to unicode chars in the string)

CSS_UIKIT_2_27_1_STYLE_OFFLINE = """

/*! UIkit 2.27.1 | http://www.getuikit.com | (c) 2014 YOOtheme | MIT License */
/* ========================================================================
   Component: Base
 ========================================================================== */
/*
 * 1. Normalize default `font-family` and set `font-size` to support `rem` units
 * 2. Prevents iOS text size adjust after orientation change, without disabling user zoom
 * 3. Style
 */
html {
  /* 1 */
  font: normal 14px / 20px "Helvetica Neue", Helvetica, Arial, sans-serif;
  /* 2 */
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
  /* 3 */
  background: #fff;
  /* color customized - #444 -> #000 */
  color: #000;
  background-image: -webkit-radial-gradient(100% 100%, center, #fff, #fff);
  background-image: radial-gradient(100% 100% at center, #fff, #fff);
}
/*
 * Removes default margin.
 */
body {
  margin: 0;
}
/* Links
 ========================================================================== */
/*
 * Remove the gray background color from active links in IE 10.
 */
a {
  background: transparent;
}
/*
 * Improve readability of focused elements when they are also in an active/hover state.
 */
a:active,
a:hover {
  outline: 0;
}
/*
 * Style
 */
a,
.uk-link {
  /* color customized - #07D -> #009 */
  color: #009;
  text-decoration: none;
  cursor: pointer;
}
a:hover,
.uk-link:hover {
  color: #059;
  text-decoration: underline;
}
/* Text-level semantics
 ========================================================================== */
/*
 * Address styling not present in IE 8/9/10/11, Safari, and Chrome.
 */
abbr[title] {
  border-bottom: 1px dotted;
}
/*
 * Address style set to `bolder` in Firefox 4+, Safari, and Chrome.
 */
b,
strong {
  font-weight: bold;
}
/*
 * 1. Address odd `em`-unit font size rendering in all browsers.
 * 2. Consolas has a better baseline in running text compared to `Courier`
 */
:not(pre) > code,
:not(pre) > kbd,
:not(pre) > samp {
  /* 1 */
  font-size: 12px;
  /* 2 */
  font-family: Consolas, monospace, serif;
  /* 3 */
  color: #D05;
  white-space: nowrap;
  padding: 0 4px;
  border: 1px solid #ddd;
  border-radius: 3px;
  background: #fafafa;
}
/*
 * Emphasize
 */
em {
  color: #D05;
}
/*
 * Insert
 */
ins {
  background: #ffa;
  color: #444;
  text-decoration: none;
}
/*
 * Mark
 * Note: Addresses styling not present in IE 8/9.
 */
mark {
  background: #ffa;
  color: #444;
}
/*
 * Quote
 */
q {
  font-style: italic;
}
/*
 * Addresses inconsistent and variable font size in all browsers.
 */
small {
  font-size: 80%;
}
/*
 * Prevents `sub` and `sup` affecting `line-height` in all browsers.
 */
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
/* Embedded content
 ========================================================================== */
/*
 * Remove the gap between embedded content and the bottom of their containers.
 */
audio,
canvas,
iframe,
img,
svg,
video {
  vertical-align: middle;
}
/*
 * Responsiveness
 * 1. Sets a maximum width relative to the parent and auto scales the height
 * 2. Corrects `max-width` behavior if padding and border are used
 */
audio,
canvas,
img,
svg,
video {
  /* 1 */
  max-width: 100%;
  height: auto;
  /* 2 */
  box-sizing: border-box;
}
/*
 * Preserve original dimensions
 */
.uk-img-preserve,
.uk-img-preserve audio,
.uk-img-preserve canvas,
.uk-img-preserve img,
.uk-img-preserve svg,
.uk-img-preserve video {
  max-width: none;
}
/*
 * Remove border when inside `a` element in IE 8/9/10.
 */
img {
  border: 0;
}
/*
 * Correct overflow not hidden in IE 9/10/11.
 */
svg:not(:root) {
  overflow: hidden;
}
/* Block elements
 ========================================================================== */
/*
 * Reset margin
 */
blockquote,
figure {
  margin: 0;
}
/*
 * Margins
 */
p,
ul,
ol,
dl,
blockquote,
pre,
address,
fieldset,
figure {
  margin: 0 0 15px 0;
}
* + p,
* + ul,
* + ol,
* + dl,
* + blockquote,
* + pre,
* + address,
* + fieldset,
* + figure {
  margin-top: 15px;
}
/* Headings
 ========================================================================== */
h1,
h2,
h3,
h4,
h5,
h6 {
  margin: 0 0 15px 0;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: normal;
  color: #444;
  text-transform: none;
}
/*
 * Margins
 */
* + h1,
* + h2,
* + h3,
* + h4,
* + h5,
* + h6 {
  margin-top: 25px;
}
/*
 * Sizes
 */
h1,
.uk-h1 {
  font-size: 36px;
  line-height: 42px;
}
h2,
.uk-h2 {
  font-size: 24px;
  line-height: 30px;
}
h3,
.uk-h3 {
  font-size: 18px;
  line-height: 24px;
}
h4,
.uk-h4 {
  font-size: 16px;
  line-height: 22px;
}
h5,
.uk-h5 {
  font-size: 14px;
  line-height: 20px;
}
h6,
.uk-h6 {
  font-size: 12px;
  line-height: 18px;
}
/* Lists
 ========================================================================== */
ul,
ol {
  padding-left: 30px;
}
/*
 * Reset margin for nested lists
 */
ul > li > ul,
ul > li > ol,
ol > li > ol,
ol > li > ul {
  margin: 0;
}
/* Description lists
 ========================================================================== */
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
/* Horizontal rules
 ========================================================================== */
/*
 * 1. Address differences between Firefox and other browsers.
 * 2. Style
 */
hr {
  /* 1 */
  box-sizing: content-box;
  height: 0;
  /* 2 */
  margin: 15px 0;
  border: 0;
  border-top: 1px solid #ddd;
}
/* Address
 ========================================================================== */
address {
  font-style: normal;
}
/* Blockquotes
 ========================================================================== */
blockquote {
  padding-left: 15px;
  border-left: 5px solid #ddd;
  font-size: 16px;
  line-height: 22px;
  font-style: italic;
}
/* Preformatted text
 ========================================================================== */
/*
 * 1. Contain overflow in all browsers.
 */
pre {
  padding: 10px;
  background: #fafafa;
  font: 12px / 18px Consolas, monospace, serif;
  color: #444;
  -moz-tab-size: 4;
  tab-size: 4;
  /* 1 */
  overflow: auto;
  border: 1px solid #ddd;
  border-radius: 3px;
}
/* Selection pseudo-element
 ========================================================================== */
::-moz-selection {
  background: #39f;
  color: #fff;
  text-shadow: none;
}
::selection {
  background: #39f;
  color: #fff;
  text-shadow: none;
}
/* HTML5 elements
 ========================================================================== */
/*
 * Correct `block` display not defined for any HTML5 element in IE 8/9.
 * Correct `block` display not defined for `details` or `summary` in IE 10/11 and Firefox.
 * Correct `block` display not defined for `main` in IE 11.
 */
article,
aside,
details,
figcaption,
figure,
footer,
header,
main,
nav,
section,
summary {
  display: block;
}
/*
 * Normalize vertical alignment of `progress` in Chrome, Firefox, and Opera.
 */
progress {
  vertical-align: baseline;
}
/*
 * Prevent displaying `audio` without controls in Chrome, Safari and Opera
 */
audio:not([controls]) {
  display: none;
}
/*
 * Address `[hidden]` styling not present in IE 8/9/10.
 * Hide the `template` element in IE 8/9/10/11, Safari, and Firefox < 22.
 */
[hidden],
template {
  display: none;
}
/* Iframe
 ========================================================================== */
iframe {
  border: 0;
}
/* Fix viewport for IE10 snap mode
 ========================================================================== */
@media screen and (max-width: 400px) {
  @-ms-viewport {
    width: device-width;
  }
}
/* ========================================================================
   Component: Grid
 ========================================================================== */
/*
 * 1. Makes grid more robust so that it can be used with other block elements like lists
 */
.uk-grid {
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -ms-flex-wrap: wrap;
  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;
  /* 1 */
  margin: 0;
  padding: 0;
  list-style: none;
}
/*
 * DEPRECATED
 * Micro clearfix
 * Can't use `table` because it creates a 1px gap when it becomes a flex item, only in Webkit
 */
.uk-grid:before,
.uk-grid:after {
  content: "";
  display: block;
  overflow: hidden;
}
.uk-grid:after {
  clear: both;
}
/*
 * Grid cell
 * 1. Space is allocated solely based on content dimensions
 * 2. Makes grid more robust so that it can be used with other block elements
 * 3. DEPRECATED Using `float` to support IE9
 */
.uk-grid > * {
  /* 1 */
  -ms-flex: none;
  -webkit-flex: none;
  flex: none;
  /* 2 */
  margin: 0;
  /* 3 */
  float: left;
}
/*
 * Remove margin from the last-child
 */
.uk-grid > * > :last-child {
  margin-bottom: 0;
}
/* Grid gutter
 ========================================================================== */
/*
 * Default gutter
 */
/* Horizontal */
.uk-grid {
  margin-left: -25px;
}
.uk-grid > * {
  padding-left: 25px;
}
/* Vertical */
.uk-grid + .uk-grid,
.uk-grid-margin,
.uk-grid > * > .uk-panel + .uk-panel {
  margin-top: 25px;
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  /* Horizontal */
  .uk-grid {
    margin-left: -35px;
  }
  .uk-grid > * {
    padding-left: 35px;
  }
  /* Vertical */
  .uk-grid + .uk-grid,
  .uk-grid-margin,
  .uk-grid > * > .uk-panel + .uk-panel {
    margin-top: 35px;
  }
}
/*
 * Collapse gutter
 */
/* Horizontal */
.uk-grid-collapse {
  margin-left: 0;
}
.uk-grid-collapse > * {
  padding-left: 0;
}
/* Vertical */
.uk-grid-collapse + .uk-grid-collapse,
.uk-grid-collapse > .uk-grid-margin,
.uk-grid-collapse > * > .uk-panel + .uk-panel {
  margin-top: 0;
}
/*
 * Small gutter
 */
/* Horizontal */
.uk-grid-small {
  margin-left: -10px;
}
.uk-grid-small > * {
  padding-left: 10px;
}
/* Vertical */
.uk-grid-small + .uk-grid-small,
.uk-grid-small > .uk-grid-margin,
.uk-grid-small > * > .uk-panel + .uk-panel {
  margin-top: 10px;
}
/*
 * Medium gutter
 */
/* Horizontal */
.uk-grid-medium {
  margin-left: -25px;
}
.uk-grid-medium > * {
  padding-left: 25px;
}
/* Vertical */
.uk-grid-medium + .uk-grid-medium,
.uk-grid-medium > .uk-grid-margin,
.uk-grid-medium > * > .uk-panel + .uk-panel {
  margin-top: 25px;
}
/*
 * Large gutter
 */
/* Large screen and bigger */
@media (min-width: 960px) {
  /* Horizontal */
  .uk-grid-large {
    margin-left: -35px;
  }
  .uk-grid-large > * {
    padding-left: 35px;
  }
  /* Vertical */
  .uk-grid-large + .uk-grid-large,
  .uk-grid-large-margin,
  .uk-grid-large > * > .uk-panel + .uk-panel {
    margin-top: 35px;
  }
}
/* Extra Large screens */
@media (min-width: 1220px) {
  /* Horizontal */
  .uk-grid-large {
    margin-left: -50px;
  }
  .uk-grid-large > * {
    padding-left: 50px;
  }
  /* Vertical */
  .uk-grid-large + .uk-grid-large,
  .uk-grid-large-margin,
  .uk-grid-large > * > .uk-panel + .uk-panel {
    margin-top: 50px;
  }
}
/* Modifier: `uk-grid-divider`
 ========================================================================== */
/*
 * Horizontal divider
 * Only works with the default gutter. Does not work with gutter collapse, small or large.
 * Does not work with `uk-push-*`, `uk-pull-*` and not if the columns float into the next row.
 */
.uk-grid-divider:not(:empty) {
  margin-left: -25px;
  margin-right: -25px;
}
.uk-grid-divider > * {
  padding-left: 25px;
  padding-right: 25px;
}
.uk-grid-divider > [class*='uk-width-1-']:not(.uk-width-1-1):nth-child(n+2),
.uk-grid-divider > [class*='uk-width-2-']:nth-child(n+2),
.uk-grid-divider > [class*='uk-width-3-']:nth-child(n+2),
.uk-grid-divider > [class*='uk-width-4-']:nth-child(n+2),
.uk-grid-divider > [class*='uk-width-5-']:nth-child(n+2),
.uk-grid-divider > [class*='uk-width-6-']:nth-child(n+2),
.uk-grid-divider > [class*='uk-width-7-']:nth-child(n+2),
.uk-grid-divider > [class*='uk-width-8-']:nth-child(n+2),
.uk-grid-divider > [class*='uk-width-9-']:nth-child(n+2) {
  border-left: 1px solid #ddd;
}
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-grid-divider > [class*='uk-width-medium-']:not(.uk-width-medium-1-1):nth-child(n+2) {
    border-left: 1px solid #ddd;
  }
}
/* Desktop and bigger */
@media (min-width: 960px) {
  .uk-grid-divider > [class*='uk-width-large-']:not(.uk-width-large-1-1):nth-child(n+2) {
    border-left: 1px solid #ddd;
  }
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  /*
     * Large gutter
     */
  .uk-grid-divider:not(:empty) {
    margin-left: -35px;
    margin-right: -35px;
  }
  .uk-grid-divider > * {
    padding-left: 35px;
    padding-right: 35px;
  }
  .uk-grid-divider:empty {
    margin-top: 35px;
    margin-bottom: 35px;
  }
}
/*
 * Vertical divider
 */
.uk-grid-divider:empty {
  margin-top: 25px;
  margin-bottom: 25px;
  border-top: 1px solid #ddd;
}
/* Match panels in grids
 ========================================================================== */
/*
 * 1. Behave like a block element
 */
.uk-grid-match > * {
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  /* 1 */
  -ms-flex-wrap: wrap;
  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;
}
.uk-grid-match > * > * {
  /* 1 */
  -ms-flex: none;
  -webkit-flex: none;
  flex: none;
  box-sizing: border-box;
  width: 100%;
}
/* Even grid cell widths
 ========================================================================== */
[class*='uk-grid-width'] > * {
  box-sizing: border-box;
  width: 100%;
}
.uk-grid-width-1-2 > * {
  width: 50%;
}
.uk-grid-width-1-3 > * {
  width: 33.333%;
}
.uk-grid-width-1-4 > * {
  width: 25%;
}
.uk-grid-width-1-5 > * {
  width: 20%;
}
.uk-grid-width-1-6 > * {
  width: 16.666%;
}
.uk-grid-width-1-10 > * {
  width: 10%;
}
.uk-grid-width-auto > * {
  width: auto;
}
/* Phone landscape and bigger */
@media (min-width: 480px) {
  .uk-grid-width-small-1-1 > * {
    width: 100%;
  }
  .uk-grid-width-small-1-2 > * {
    width: 50%;
  }
  .uk-grid-width-small-1-3 > * {
    width: 33.333%;
  }
  .uk-grid-width-small-1-4 > * {
    width: 25%;
  }
  .uk-grid-width-small-1-5 > * {
    width: 20%;
  }
  .uk-grid-width-small-1-6 > * {
    width: 16.666%;
  }
  .uk-grid-width-small-1-10 > * {
    width: 10%;
  }
}
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-grid-width-medium-1-1 > * {
    width: 100%;
  }
  .uk-grid-width-medium-1-2 > * {
    width: 50%;
  }
  .uk-grid-width-medium-1-3 > * {
    width: 33.333%;
  }
  .uk-grid-width-medium-1-4 > * {
    width: 25%;
  }
  .uk-grid-width-medium-1-5 > * {
    width: 20%;
  }
  .uk-grid-width-medium-1-6 > * {
    width: 16.666%;
  }
  .uk-grid-width-medium-1-10 > * {
    width: 10%;
  }
}
/* Desktop and bigger */
@media (min-width: 960px) {
  .uk-grid-width-large-1-1 > * {
    width: 100%;
  }
  .uk-grid-width-large-1-2 > * {
    width: 50%;
  }
  .uk-grid-width-large-1-3 > * {
    width: 33.333%;
  }
  .uk-grid-width-large-1-4 > * {
    width: 25%;
  }
  .uk-grid-width-large-1-5 > * {
    width: 20%;
  }
  .uk-grid-width-large-1-6 > * {
    width: 16.666%;
  }
  .uk-grid-width-large-1-10 > * {
    width: 10%;
  }
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  .uk-grid-width-xlarge-1-1 > * {
    width: 100%;
  }
  .uk-grid-width-xlarge-1-2 > * {
    width: 50%;
  }
  .uk-grid-width-xlarge-1-3 > * {
    width: 33.333%;
  }
  .uk-grid-width-xlarge-1-4 > * {
    width: 25%;
  }
  .uk-grid-width-xlarge-1-5 > * {
    width: 20%;
  }
  .uk-grid-width-xlarge-1-6 > * {
    width: 16.666%;
  }
  .uk-grid-width-xlarge-1-10 > * {
    width: 10%;
  }
}
/* Sub-objects: `uk-width-*`
 ========================================================================== */
[class*='uk-width'] {
  box-sizing: border-box;
  width: 100%;
}
/*
 * Widths
 */
/* Whole */
.uk-width-1-1 {
  width: 100%;
}
/* Halves */
.uk-width-1-2,
.uk-width-2-4,
.uk-width-3-6,
.uk-width-5-10 {
  width: 50%;
}
/* Thirds */
.uk-width-1-3,
.uk-width-2-6 {
  width: 33.333%;
}
.uk-width-2-3,
.uk-width-4-6 {
  width: 66.666%;
}
/* Quarters */
.uk-width-1-4 {
  width: 25%;
}
.uk-width-3-4 {
  width: 75%;
}
/* Fifths */
.uk-width-1-5,
.uk-width-2-10 {
  width: 20%;
}
.uk-width-2-5,
.uk-width-4-10 {
  width: 40%;
}
.uk-width-3-5,
.uk-width-6-10 {
  width: 60%;
}
.uk-width-4-5,
.uk-width-8-10 {
  width: 80%;
}
/* Sixths */
.uk-width-1-6 {
  width: 16.666%;
}
.uk-width-5-6 {
  width: 83.333%;
}
/* Tenths */
.uk-width-1-10 {
  width: 10%;
}
.uk-width-3-10 {
  width: 30%;
}
.uk-width-7-10 {
  width: 70%;
}
.uk-width-9-10 {
  width: 90%;
}
/* Phone landscape and bigger */
@media (min-width: 480px) {
  /* Whole */
  .uk-width-small-1-1 {
    width: 100%;
  }
  /* Halves */
  .uk-width-small-1-2,
  .uk-width-small-2-4,
  .uk-width-small-3-6,
  .uk-width-small-5-10 {
    width: 50%;
  }
  /* Thirds */
  .uk-width-small-1-3,
  .uk-width-small-2-6 {
    width: 33.333%;
  }
  .uk-width-small-2-3,
  .uk-width-small-4-6 {
    width: 66.666%;
  }
  /* Quarters */
  .uk-width-small-1-4 {
    width: 25%;
  }
  .uk-width-small-3-4 {
    width: 75%;
  }
  /* Fifths */
  .uk-width-small-1-5,
  .uk-width-small-2-10 {
    width: 20%;
  }
  .uk-width-small-2-5,
  .uk-width-small-4-10 {
    width: 40%;
  }
  .uk-width-small-3-5,
  .uk-width-small-6-10 {
    width: 60%;
  }
  .uk-width-small-4-5,
  .uk-width-small-8-10 {
    width: 80%;
  }
  /* Sixths */
  .uk-width-small-1-6 {
    width: 16.666%;
  }
  .uk-width-small-5-6 {
    width: 83.333%;
  }
  /* Tenths */
  .uk-width-small-1-10 {
    width: 10%;
  }
  .uk-width-small-3-10 {
    width: 30%;
  }
  .uk-width-small-7-10 {
    width: 70%;
  }
  .uk-width-small-9-10 {
    width: 90%;
  }
}
/* Tablet and bigger */
@media (min-width: 768px) {
  /* Whole */
  .uk-width-medium-1-1 {
    width: 100%;
  }
  /* Halves */
  .uk-width-medium-1-2,
  .uk-width-medium-2-4,
  .uk-width-medium-3-6,
  .uk-width-medium-5-10 {
    width: 50%;
  }
  /* Thirds */
  .uk-width-medium-1-3,
  .uk-width-medium-2-6 {
    width: 33.333%;
  }
  .uk-width-medium-2-3,
  .uk-width-medium-4-6 {
    width: 66.666%;
  }
  /* Quarters */
  .uk-width-medium-1-4 {
    width: 25%;
  }
  .uk-width-medium-3-4 {
    width: 75%;
  }
  /* Fifths */
  .uk-width-medium-1-5,
  .uk-width-medium-2-10 {
    width: 20%;
  }
  .uk-width-medium-2-5,
  .uk-width-medium-4-10 {
    width: 40%;
  }
  .uk-width-medium-3-5,
  .uk-width-medium-6-10 {
    width: 60%;
  }
  .uk-width-medium-4-5,
  .uk-width-medium-8-10 {
    width: 80%;
  }
  /* Sixths */
  .uk-width-medium-1-6 {
    width: 16.666%;
  }
  .uk-width-medium-5-6 {
    width: 83.333%;
  }
  /* Tenths */
  .uk-width-medium-1-10 {
    width: 10%;
  }
  .uk-width-medium-3-10 {
    width: 30%;
  }
  .uk-width-medium-7-10 {
    width: 70%;
  }
  .uk-width-medium-9-10 {
    width: 90%;
  }
}
/* Desktop and bigger */
@media (min-width: 960px) {
  /* Whole */
  .uk-width-large-1-1 {
    width: 100%;
  }
  /* Halves */
  .uk-width-large-1-2,
  .uk-width-large-2-4,
  .uk-width-large-3-6,
  .uk-width-large-5-10 {
    width: 50%;
  }
  /* Thirds */
  .uk-width-large-1-3,
  .uk-width-large-2-6 {
    width: 33.333%;
  }
  .uk-width-large-2-3,
  .uk-width-large-4-6 {
    width: 66.666%;
  }
  /* Quarters */
  .uk-width-large-1-4 {
    width: 25%;
  }
  .uk-width-large-3-4 {
    width: 75%;
  }
  /* Fifths */
  .uk-width-large-1-5,
  .uk-width-large-2-10 {
    width: 20%;
  }
  .uk-width-large-2-5,
  .uk-width-large-4-10 {
    width: 40%;
  }
  .uk-width-large-3-5,
  .uk-width-large-6-10 {
    width: 60%;
  }
  .uk-width-large-4-5,
  .uk-width-large-8-10 {
    width: 80%;
  }
  /* Sixths */
  .uk-width-large-1-6 {
    width: 16.666%;
  }
  .uk-width-large-5-6 {
    width: 83.333%;
  }
  /* Tenths */
  .uk-width-large-1-10 {
    width: 10%;
  }
  .uk-width-large-3-10 {
    width: 30%;
  }
  .uk-width-large-7-10 {
    width: 70%;
  }
  .uk-width-large-9-10 {
    width: 90%;
  }
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  /* Whole */
  .uk-width-xlarge-1-1 {
    width: 100%;
  }
  /* Halves */
  .uk-width-xlarge-1-2,
  .uk-width-xlarge-2-4,
  .uk-width-xlarge-3-6,
  .uk-width-xlarge-5-10 {
    width: 50%;
  }
  /* Thirds */
  .uk-width-xlarge-1-3,
  .uk-width-xlarge-2-6 {
    width: 33.333%;
  }
  .uk-width-xlarge-2-3,
  .uk-width-xlarge-4-6 {
    width: 66.666%;
  }
  /* Quarters */
  .uk-width-xlarge-1-4 {
    width: 25%;
  }
  .uk-width-xlarge-3-4 {
    width: 75%;
  }
  /* Fifths */
  .uk-width-xlarge-1-5,
  .uk-width-xlarge-2-10 {
    width: 20%;
  }
  .uk-width-xlarge-2-5,
  .uk-width-xlarge-4-10 {
    width: 40%;
  }
  .uk-width-xlarge-3-5,
  .uk-width-xlarge-6-10 {
    width: 60%;
  }
  .uk-width-xlarge-4-5,
  .uk-width-xlarge-8-10 {
    width: 80%;
  }
  /* Sixths */
  .uk-width-xlarge-1-6 {
    width: 16.666%;
  }
  .uk-width-xlarge-5-6 {
    width: 83.333%;
  }
  /* Tenths */
  .uk-width-xlarge-1-10 {
    width: 10%;
  }
  .uk-width-xlarge-3-10 {
    width: 30%;
  }
  .uk-width-xlarge-7-10 {
    width: 70%;
  }
  .uk-width-xlarge-9-10 {
    width: 90%;
  }
}
/* Sub-object: `uk-push-*` and `uk-pull-*`
 ========================================================================== */
/*
 * Source ordering
 * Works only with `uk-width-medium-*`
 */
/* Tablet and bigger */
@media (min-width: 768px) {
  [class*='uk-push-'],
  [class*='uk-pull-'] {
    position: relative;
  }
  /*
     * Push
     */
  /* Halves */
  .uk-push-1-2,
  .uk-push-2-4,
  .uk-push-3-6,
  .uk-push-5-10 {
    left: 50%;
  }
  /* Thirds */
  .uk-push-1-3,
  .uk-push-2-6 {
    left: 33.333%;
  }
  .uk-push-2-3,
  .uk-push-4-6 {
    left: 66.666%;
  }
  /* Quarters */
  .uk-push-1-4 {
    left: 25%;
  }
  .uk-push-3-4 {
    left: 75%;
  }
  /* Fifths */
  .uk-push-1-5,
  .uk-push-2-10 {
    left: 20%;
  }
  .uk-push-2-5,
  .uk-push-4-10 {
    left: 40%;
  }
  .uk-push-3-5,
  .uk-push-6-10 {
    left: 60%;
  }
  .uk-push-4-5,
  .uk-push-8-10 {
    left: 80%;
  }
  /* Sixths */
  .uk-push-1-6 {
    left: 16.666%;
  }
  .uk-push-5-6 {
    left: 83.333%;
  }
  /* Tenths */
  .uk-push-1-10 {
    left: 10%;
  }
  .uk-push-3-10 {
    left: 30%;
  }
  .uk-push-7-10 {
    left: 70%;
  }
  .uk-push-9-10 {
    left: 90%;
  }
  /*
     * Pull
     */
  /* Halves */
  .uk-pull-1-2,
  .uk-pull-2-4,
  .uk-pull-3-6,
  .uk-pull-5-10 {
    left: -50%;
  }
  /* Thirds */
  .uk-pull-1-3,
  .uk-pull-2-6 {
    left: -33.333%;
  }
  .uk-pull-2-3,
  .uk-pull-4-6 {
    left: -66.666%;
  }
  /* Quarters */
  .uk-pull-1-4 {
    left: -25%;
  }
  .uk-pull-3-4 {
    left: -75%;
  }
  /* Fifths */
  .uk-pull-1-5,
  .uk-pull-2-10 {
    left: -20%;
  }
  .uk-pull-2-5,
  .uk-pull-4-10 {
    left: -40%;
  }
  .uk-pull-3-5,
  .uk-pull-6-10 {
    left: -60%;
  }
  .uk-pull-4-5,
  .uk-pull-8-10 {
    left: -80%;
  }
  /* Sixths */
  .uk-pull-1-6 {
    left: -16.666%;
  }
  .uk-pull-5-6 {
    left: -83.333%;
  }
  /* Tenths */
  .uk-pull-1-10 {
    left: -10%;
  }
  .uk-pull-3-10 {
    left: -30%;
  }
  .uk-pull-7-10 {
    left: -70%;
  }
  .uk-pull-9-10 {
    left: -90%;
  }
}
/* ========================================================================
   Component: Panel
 ========================================================================== */
/*
 * 1. Needed for `a` elements
 * 2. Create position context for badges
 */
.uk-panel {
  /* 1 */
  display: block;
  /* 2 */
  position: relative;
}
/*
 * Allow panels to be anchors
 */
.uk-panel,
.uk-panel:hover {
  text-decoration: none;
}
/*
 * Micro clearfix to make panels more robust
 */
.uk-panel:before,
.uk-panel:after {
  content: "";
  display: table;
}
.uk-panel:after {
  clear: both;
}
/*
 * Remove margin from the last-child if not `uk-widget-title`
 */
.uk-panel > :not(.uk-panel-title):last-child {
  margin-bottom: 0;
}
/* Sub-object: `uk-panel-title`
 ========================================================================== */
.uk-panel-title {
  margin-top: 0;
  margin-bottom: 15px;
  font-size: 18px;
  line-height: 24px;
  font-weight: normal;
  text-transform: none;
  color: #444;
}
/* Sub-object: `uk-panel-badge`
 ========================================================================== */
.uk-panel-badge {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 1;
}
/* Sub-object: `uk-panel-teaser`
 ========================================================================== */
.uk-panel-teaser {
  margin-bottom: 15px;
}
/* Sub-object: `uk-panel-body`
 ========================================================================== */
.uk-panel-body {
  padding: 15px;
}
/* Modifier: `uk-panel-box`
 ========================================================================== */
.uk-panel-box {
  padding: 15px;
  background: #fafafa;
  color: #444;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.uk-panel-box-hover:hover {
  color: #444;
}
.uk-panel-box .uk-panel-title {
  color: #444;
}
.uk-panel-box .uk-panel-badge {
  top: 10px;
  right: 10px;
}
.uk-panel-box > .uk-panel-teaser {
  margin-top: -16px;
  margin-left: -16px;
  margin-right: -16px;
}
/*
 * Nav in panel
 */
.uk-panel-box > .uk-nav-side {
  margin: 0 -15px;
}
/*
 * Sub-modifier: `uk-panel-box-primary`
 */
.uk-panel-box-primary {
  background-color: #ebf7fd;
  color: #2d7091;
  border-color: rgba(45, 112, 145, 0.3);
}
.uk-panel-box-primary-hover:hover {
  color: #2d7091;
}
.uk-panel-box-primary .uk-panel-title {
  color: #2d7091;
}
/*
 * Sub-modifier: `uk-panel-box-secondary`
 */
.uk-panel-box-secondary {
  background-color: #fff;
  color: #444;
}
.uk-panel-box-secondary-hover:hover {
  color: #444;
}
.uk-panel-box-secondary .uk-panel-title {
  color: #444;
}
/* Modifier: `uk-panel-hover`
 ========================================================================== */
.uk-panel-hover {
  padding: 15px;
  color: #444;
  border: 1px solid transparent;
  border-radius: 4px;
}
.uk-panel-hover:hover {
  background: #fafafa;
  color: #444;
  border-color: #ddd;
}
.uk-panel-hover .uk-panel-badge {
  top: 10px;
  right: 10px;
}
.uk-panel-hover > .uk-panel-teaser {
  margin-top: -16px;
  margin-left: -16px;
  margin-right: -16px;
}
/* Modifier: `uk-panel-header`
 ========================================================================== */
.uk-panel-header .uk-panel-title {
  padding-bottom: 10px;
  border-bottom: 1px solid #ddd;
  color: #444;
}
/* Modifier: `uk-panel-space`
 ========================================================================== */
.uk-panel-space {
  padding: 30px;
}
.uk-panel-space .uk-panel-badge {
  top: 30px;
  right: 30px;
}
/* Modifier: `uk-panel-divider`
 ========================================================================== */
.uk-panel + .uk-panel-divider {
  margin-top: 50px !important;
}
.uk-panel + .uk-panel-divider:before {
  content: "";
  display: block;
  position: absolute;
  top: -25px;
  left: 0;
  right: 0;
  border-top: 1px solid #ddd;
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  .uk-panel + .uk-panel-divider {
    margin-top: 70px !important;
  }
  .uk-panel + .uk-panel-divider:before {
    top: -35px;
  }
}
.uk-panel-box .uk-panel-teaser {
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  overflow: hidden;
  -webkit-transform: translateZ(0);
}
/* ========================================================================
   Component: Block
 ========================================================================== */
.uk-block {
  position: relative;
  box-sizing: border-box;
  padding-top: 20px;
  padding-bottom: 20px;
}
/* Phone landscape and bigger */
@media (min-width: 768px) {
  .uk-block {
    padding-top: 50px;
    padding-bottom: 50px;
  }
}
/*
 * Micro clearfix to make blocks more robust
 */
.uk-block:before,
.uk-block:after {
  content: "";
  display: table;
}
.uk-block:after {
  clear: both;
}
/*
 * Remove margin from the last-child
 */
.uk-block > :last-child {
  margin-bottom: 0;
}
/* Padding Modifier
 ========================================================================== */
/*
 * Large padding
 */
.uk-block-large {
  padding-top: 20px;
  padding-bottom: 20px;
}
/* Tablets and bigger */
@media (min-width: 768px) {
  .uk-block-large {
    padding-top: 50px;
    padding-bottom: 50px;
  }
}
/* Desktop and bigger */
@media (min-width: 960px) {
  .uk-block-large {
    padding-top: 100px;
    padding-bottom: 100px;
  }
}
/* Color Modifier
 ========================================================================== */
/*
 * Default
 */
.uk-block-default {
  background: #fff;
}
/*
 * Muted
 */
.uk-block-muted {
  background: #f9f9f9;
}
/*
 * Primary
 */
.uk-block-primary {
  background: #00a8e6;
}
/*
 * Secondary
 */
.uk-block-secondary {
  background: #222;
}
/*
     * Adjust padding between equal colored blocks
     */
.uk-block-default + .uk-block-default,
.uk-block-muted + .uk-block-muted,
.uk-block-primary + .uk-block-primary,
.uk-block-secondary + .uk-block-secondary {
  padding-top: 0;
}
/* ========================================================================
   Component: Article
 ========================================================================== */
/*
 * Micro clearfix to make articles more robust
 */
.uk-article:before,
.uk-article:after {
  content: "";
  display: table;
}
.uk-article:after {
  clear: both;
}
/*
 * Remove margin from the last-child
 */
.uk-article > :last-child {
  margin-bottom: 0;
}
/*
 * Vertical gutter for articles
 */
.uk-article + .uk-article {
  margin-top: 25px;
}
/* Sub-object `uk-article-title`
 ========================================================================== */
.uk-article-title {
  font-size: 36px;
  line-height: 42px;
  font-weight: normal;
  text-transform: none;
}
.uk-article-title a {
  color: inherit;
  text-decoration: none;
}
/* Sub-object `uk-article-meta`
 ========================================================================== */
.uk-article-meta {
  font-size: 12px;
  line-height: 18px;
  color: #999;
}
/* Sub-object `uk-article-lead`
 ========================================================================== */
.uk-article-lead {
  color: #444;
  font-size: 18px;
  line-height: 24px;
  font-weight: normal;
}
/* Sub-object `uk-article-divider`
 ========================================================================== */
.uk-article-divider {
  margin-bottom: 25px;
  border-color: #ddd;
}
* + .uk-article-divider {
  margin-top: 25px;
}
.uk-article + .uk-article {
  padding-top: 25px;
  border-top: 1px solid #ddd;
}
/* ========================================================================
   Component: Comment
 ========================================================================== */
/* Sub-object `uk-comment-header`
 ========================================================================== */
.uk-comment-header {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: #fafafa;
}
/*
 * Micro clearfix
 */
.uk-comment-header:before,
.uk-comment-header:after {
  content: "";
  display: table;
}
.uk-comment-header:after {
  clear: both;
}
/* Sub-object `uk-comment-avatar`
 ========================================================================== */
.uk-comment-avatar {
  margin-right: 15px;
  float: left;
}
/* Sub-object `uk-comment-title`
 ========================================================================== */
.uk-comment-title {
  margin: 5px 0 0 0;
  font-size: 16px;
  line-height: 22px;
}
/* Sub-object `uk-comment-meta`
 ========================================================================== */
.uk-comment-meta {
  margin: 2px 0 0 0;
  font-size: 11px;
  line-height: 16px;
  color: #999;
}
/* Sub-object `uk-comment-body`
 ========================================================================== */
.uk-comment-body {
  padding-left: 10px;
  padding-right: 10px;
}
/*
 * Remove margin from the last-child
 */
.uk-comment-body > :last-child {
  margin-bottom: 0;
}
/* Sub-object `uk-comment-list`
 ========================================================================== */
.uk-comment-list {
  padding: 0;
  list-style: none;
}
.uk-comment-list .uk-comment + ul {
  margin: 25px 0 0 0;
  list-style: none;
}
.uk-comment-list > li:nth-child(n+2),
.uk-comment-list .uk-comment + ul > li:nth-child(n+2) {
  margin-top: 25px;
}
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-comment-list .uk-comment + ul {
    padding-left: 100px;
  }
}
/* Modifier `uk-comment-primary`
 ========================================================================== */
.uk-comment-primary .uk-comment-header {
  border-color: rgba(45, 112, 145, 0.3);
  background-color: #ebf7fd;
  color: #2d7091;
  text-shadow: 0 1px 0 #fff;
}
/* ========================================================================
   Component: Cover
 ========================================================================== */
/*
 * Background image always covers and centers its element
 */
.uk-cover-background {
  background-position: 50% 50%;
  background-size: cover;
  background-repeat: no-repeat;
}
/*
 * Emulates image cover, works with video and image elements
 * 1. Parent container which clips resized object
 * 2. Resizes the object to always covers its container
 * 3. Reset the responsive image CSS
 * 4. Center object
 */
/* 1 */
.uk-cover {
  overflow: hidden;
}
.uk-cover-object {
  /* 2 */
  width: auto;
  height: auto;
  min-width: 100%;
  min-height: 100%;
  /* 3 */
  max-width: none;
  /* 4 */
  position: relative;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
/*
 * To center iframes use `data-uk-cover` JavaScript
 */
[data-uk-cover] {
  position: relative;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
/* ========================================================================
   Component: Nav
 ========================================================================== */
.uk-nav,
.uk-nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
/*
 * Items
 */
.uk-nav li > a {
  display: block;
  text-decoration: none;
}
.uk-nav > li > a {
  padding: 5px 15px;
}
/*
 * Nested items
 */
.uk-nav ul {
  padding-left: 15px;
}
.uk-nav ul a {
  padding: 2px 0;
}
/*
 * Item subtitle
 */
.uk-nav li > a > div {
  font-size: 12px;
  line-height: 18px;
}
/* Sub-object: `uk-nav-header`
 ========================================================================== */
.uk-nav-header {
  padding: 5px 15px;
  text-transform: uppercase;
  font-weight: bold;
  font-size: 12px;
}
.uk-nav-header:not(:first-child) {
  margin-top: 15px;
}
/* Sub-object: `uk-nav-divider`
 ========================================================================== */
.uk-nav-divider {
  margin: 9px 15px;
}
/* Sub-object: `uk-nav-sub`
 ========================================================================== */
/*
 * `ul` needed for higher specificity to override padding
 */
ul.uk-nav-sub {
  padding: 5px 0 5px 15px;
}
/* Modifier: `uk-nav-parent-icon`
 ========================================================================== */
.uk-nav-parent-icon > .uk-parent > a:after {
  content: "\\f104";
  width: 20px;
  margin-right: -10px;
  float: right;
  font-family: FontAwesome;
  text-align: center;
}
.uk-nav-parent-icon > .uk-parent.uk-open > a:after {
  content: "\\f107";
}
/* Modifier `uk-nav-side`
 ========================================================================== */
/*
 * Items
 */
.uk-nav-side > li > a {
  color: #444;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-nav-side > li > a:hover,
.uk-nav-side > li > a:focus {
  background: rgba(0, 0, 0, 0.03);
  color: #444;
  /* 2 */
  outline: none;
  box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.1);
  text-shadow: 0 -1px 0 #fff;
}
/* Active */
.uk-nav-side > li.uk-active > a {
  background: #009dd8;
  color: #fff;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
}
/*
 * Sub-object: `uk-nav-header`
 */
.uk-nav-side .uk-nav-header {
  color: #444;
}
/*
 * Sub-object: `uk-nav-divider`
 */
.uk-nav-side .uk-nav-divider {
  border-top: 1px solid #ddd;
  box-shadow: 0 1px 0 #fff;
}
/*
 * Nested items
 */
.uk-nav-side ul a {
  color: #07D;
}
.uk-nav-side ul a:hover {
  color: #059;
}
/* Modifier `uk-nav-dropdown`
 ========================================================================== */
/*
 * Items
 */
.uk-nav-dropdown > li > a {
  color: #444;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-nav-dropdown > li > a:hover,
.uk-nav-dropdown > li > a:focus {
  background: #009dd8;
  color: #fff;
  /* 2 */
  outline: none;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
}
/*
 * Sub-object: `uk-nav-header`
 */
.uk-nav-dropdown .uk-nav-header {
  color: #999;
}
/*
 * Sub-object: `uk-nav-divider`
 */
.uk-nav-dropdown .uk-nav-divider {
  border-top: 1px solid #ddd;
}
/*
 * Nested items
 */
.uk-nav-dropdown ul a {
  color: #07D;
}
.uk-nav-dropdown ul a:hover {
  color: #059;
}
/* Modifier `uk-nav-navbar`
 ========================================================================== */
/*
 * Items
 */
.uk-nav-navbar > li > a {
  color: #444;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-nav-navbar > li > a:hover,
.uk-nav-navbar > li > a:focus {
  background: #009dd8;
  color: #fff;
  /* 2 */
  outline: none;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
}
/*
 * Sub-object: `uk-nav-header`
 */
.uk-nav-navbar .uk-nav-header {
  color: #999;
}
/*
 * Sub-object: `uk-nav-divider`
 */
.uk-nav-navbar .uk-nav-divider {
  border-top: 1px solid #ddd;
}
/*
 * Nested items
 */
.uk-nav-navbar ul a {
  color: #07D;
}
.uk-nav-navbar ul a:hover {
  color: #059;
}
/* Modifier `uk-nav-offcanvas`
 ========================================================================== */
/*
 * Items
 */
.uk-nav-offcanvas > li > a {
  color: #ccc;
  padding: 10px 15px;
  border-top: 1px solid rgba(0, 0, 0, 0.3);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
  text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
}
/*
 * Hover
 * No hover on touch devices because it behaves buggy in fixed offcanvas
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-nav-offcanvas > .uk-open > a,
html:not(.uk-touch) .uk-nav-offcanvas > li > a:hover,
html:not(.uk-touch) .uk-nav-offcanvas > li > a:focus {
  background: #404040;
  color: #fff;
  /* 2 */
  outline: none;
}
/*
 * Active
 * `html .uk-nav` needed for higher specificity to override hover
 */
html .uk-nav.uk-nav-offcanvas > li.uk-active > a {
  background: #1a1a1a;
  color: #fff;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.3);
}
/*
 * Sub-object: `uk-nav-header`
 */
.uk-nav-offcanvas .uk-nav-header {
  color: #777;
  margin-top: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.3);
  background: #404040;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
  text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
}
/*
 * Sub-object: `uk-nav-divider`
 */
.uk-nav-offcanvas .uk-nav-divider {
  border-top: 1px solid rgba(255, 255, 255, 0.01);
  margin: 0;
  height: 4px;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.3);
}
/*
 * Nested items
 * No hover on touch devices because it behaves buggy in fixed offcanvas
 */
.uk-nav-offcanvas ul a {
  color: #ccc;
}
html:not(.uk-touch) .uk-nav-offcanvas ul a:hover {
  color: #fff;
}
/*
     * Modifier `uk-nav-offcanvas`
     */
.uk-nav-offcanvas {
  border-bottom: 1px solid rgba(0, 0, 0, 0.3);
  box-shadow: 0 1px 0 rgba(255, 255, 255, 0.05);
}
/*
     * Sub-object: `uk-nav-sub`
     */
.uk-nav-offcanvas .uk-nav-sub {
  border-top: 1px solid rgba(0, 0, 0, 0.3);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
}
/* ========================================================================
   Component: Navbar
 ========================================================================== */
.uk-navbar {
  background: #f7f7f7;
  color: #444;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-bottom-color: rgba(0, 0, 0, 0.3);
  border-radius: 4px;
  background-origin: border-box;
  background-image: -webkit-linear-gradient(top, #fff, #eee);
  background-image: linear-gradient(to bottom, #fff, #eee);
}
/*
 * Micro clearfix
 */
.uk-navbar:before,
.uk-navbar:after {
  content: "";
  display: table;
}
.uk-navbar:after {
  clear: both;
}
/* Sub-object: `uk-navbar-nav`
 ========================================================================== */
.uk-navbar-nav {
  margin: 0;
  padding: 0;
  list-style: none;
  float: left;
}
/*
 * 1. Create position context for dropdowns
 */
.uk-navbar-nav > li {
  float: left;
  /* 1 */
  position: relative;
}
/*
 * 1. Dimensions
 * 2. Style
 */
.uk-navbar-nav > li > a {
  display: block;
  box-sizing: border-box;
  text-decoration: none;
  /* 1 */
  height: 41px;
  padding: 0 15px;
  line-height: 40px;
  /* 2 */
  color: #444;
  font-size: 14px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-weight: normal;
  margin-top: -1px;
  margin-left: -1px;
  border: 1px solid transparent;
  border-bottom-width: 0;
  text-shadow: 0 1px 0 #fff;
}
/* Appear not as link */
.uk-navbar-nav > li > a[href='#'] {
  cursor: text;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Also apply if dropdown is opened
 * 3. Remove default focus style
 */
.uk-navbar-nav > li:hover > a,
.uk-navbar-nav > li > a:focus,
.uk-navbar-nav > li.uk-open > a {
  background-color: transparent;
  color: #444;
  /* 3 */
  outline: none;
  position: relative;
  z-index: 1;
  border-left-color: rgba(0, 0, 0, 0.1);
  border-right-color: rgba(0, 0, 0, 0.1);
  border-top-color: rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}
/* OnClick */
.uk-navbar-nav > li > a:active {
  background-color: #f5f5f5;
  color: #444;
  border-left-color: rgba(0, 0, 0, 0.1);
  border-right-color: rgba(0, 0, 0, 0.1);
  border-top-color: rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}
/* Active */
.uk-navbar-nav > li.uk-active > a {
  background-color: #fafafa;
  color: #444;
  border-left-color: rgba(0, 0, 0, 0.1);
  border-right-color: rgba(0, 0, 0, 0.1);
  border-top-color: rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}
/* Sub-objects: `uk-navbar-nav-subtitle`
 ========================================================================== */
.uk-navbar-nav .uk-navbar-nav-subtitle {
  line-height: 28px;
}
.uk-navbar-nav-subtitle > div {
  margin-top: -6px;
  font-size: 10px;
  line-height: 12px;
}
/* Sub-objects: `uk-navbar-content`, `uk-navbar-brand`, `uk-navbar-toggle`
 ========================================================================== */
/*
 * Imitate navbar items
 */
.uk-navbar-content,
.uk-navbar-brand,
.uk-navbar-toggle {
  box-sizing: border-box;
  display: block;
  height: 41px;
  padding: 0 15px;
  float: left;
  margin-top: -1px;
  text-shadow: 0 1px 0 #fff;
}
/*
 * Helper to center all child elements vertically
 */
.uk-navbar-content:before,
.uk-navbar-brand:before,
.uk-navbar-toggle:before {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}
/* Sub-objects: `uk-navbar-content`
 ========================================================================== */
/*
 * Better sibling spacing
 */
.uk-navbar-content + .uk-navbar-content:not(.uk-navbar-center) {
  padding-left: 0;
}
/*
 * Link colors
 */
.uk-navbar-content > a:not([class]) {
  color: #07D;
}
.uk-navbar-content > a:not([class]):hover {
  color: #059;
}
/* Sub-objects: `uk-navbar-brand`
 ========================================================================== */
.uk-navbar-brand {
  font-size: 18px;
  color: #444;
  text-decoration: none;
}
/*
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-navbar-brand:hover,
.uk-navbar-brand:focus {
  color: #444;
  text-decoration: none;
  /* 2 */
  outline: none;
}
/* Sub-object: `uk-navbar-toggle`
 ========================================================================== */
.uk-navbar-toggle {
  font-size: 18px;
  color: #444;
  text-decoration: none;
}
/*
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-navbar-toggle:hover,
.uk-navbar-toggle:focus {
  color: #444;
  text-decoration: none;
  /* 2 */
  outline: none;
}
/*
 * 1. Center icon vertically
 */
.uk-navbar-toggle:after {
  content: "\\f0c9";
  font-family: FontAwesome;
  /* 1 */
  vertical-align: middle;
}
.uk-navbar-toggle-alt:after {
  content: "\\f002";
}
/* Sub-object: `uk-navbar-center`
 ========================================================================== */
/*
 * The element with this class needs to be last child in the navbar
 * 1. This hack is needed because other float elements shift centered text
 */
.uk-navbar-center {
  float: none;
  text-align: center;
  /* 1 */
  max-width: 50%;
  margin-left: auto;
  margin-right: auto;
}
/* Sub-object: `uk-navbar-flip`
 ========================================================================== */
.uk-navbar-flip {
  float: right;
}
/*
     * Apply same `border-radius` as `uk-navbar`
     */
.uk-navbar-nav:first-child > li:first-child > a {
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}
/*
     * Sub-modifier `uk-navbar-flip`
     */
/* Collapse border */
.uk-navbar-flip .uk-navbar-nav > li > a {
  margin-left: 0;
  margin-right: -1px;
}
/* Apply same `border-radius` as `uk-navbar` */
.uk-navbar-flip .uk-navbar-nav:first-child > li:first-child > a {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}
.uk-navbar-flip .uk-navbar-nav:last-child > li:last-child > a {
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}
/*
     * Sub-modifier `uk-navbar-attached`
     */
.uk-navbar-attached {
  border-top-color: transparent;
  border-left-color: transparent;
  border-right-color: transparent;
  border-radius: 0;
}
.uk-navbar-attached .uk-navbar-nav > li > a {
  border-radius: 0 !important;
}
/* ========================================================================
   Component: Subnav
 ========================================================================== */
/*
 * 1. Gutter
 * 2. Remove default list style
 */
.uk-subnav {
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -ms-flex-wrap: wrap;
  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;
  /* 1 */
  margin-left: -10px;
  margin-top: -10px;
  /* 2 */
  padding: 0;
  list-style: none;
}
/*
 * 1. Space is allocated solely based on content dimensions
 * 2. Horizontal gutter is using `padding` so `uk-width-*` classes can be applied
 * 3. Create position context for dropdowns
 */
.uk-subnav > * {
  /* 1 */
  -ms-flex: none;
  -webkit-flex: none;
  flex: none;
  /* 2 */
  padding-left: 10px;
  margin-top: 10px;
  /* 3 */
  position: relative;
}
/*
 * DEPRECATED IE9 Support
 */
.uk-subnav:before,
.uk-subnav:after {
  content: "";
  display: block;
  overflow: hidden;
}
.uk-subnav:after {
  clear: both;
}
.uk-subnav > * {
  float: left;
}
/* Items
 ========================================================================== */
.uk-subnav > * > * {
  display: inline-block;
  color: #444;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 */
.uk-subnav > * > :hover,
.uk-subnav > * > :focus {
  color: #07D;
  text-decoration: none;
}
/*
 * Active
 */
.uk-subnav > .uk-active > * {
  color: #07D;
}
/* Modifier: 'subnav-line'
 ========================================================================== */
.uk-subnav-line > :before {
  content: "";
  display: inline-block;
  height: 10px;
  vertical-align: middle;
}
.uk-subnav-line > :nth-child(n+2):before {
  margin-right: 10px;
  border-left: 1px solid #ddd;
}
/* Modifier: 'subnav-pill'
 ========================================================================== */
.uk-subnav-pill > * > * {
  padding: 3px 9px;
  border-radius: 4px;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-subnav-pill > * > :hover,
.uk-subnav-pill > * > :focus {
  background: #fafafa;
  color: #444;
  text-decoration: none;
  /* 2 */
  outline: none;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.1);
}
/*
 * Active
 * `li` needed for higher specificity to override hover
 */
.uk-subnav-pill > .uk-active > * {
  background: #009dd8;
  color: #fff;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}
/* Disabled state
 ========================================================================== */
.uk-subnav > .uk-disabled > * {
  background: none;
  color: #999;
  text-decoration: none;
  cursor: text;
  box-shadow: none;
}
/* ========================================================================
   Component: Breadcrumb
 ========================================================================== */
/*
 * 1. Remove default list style
 * 2. Remove whitespace between child elements when using `inline-block`
 */
.uk-breadcrumb {
  /* 1 */
  padding: 0;
  list-style: none;
  /* 2 */
  font-size: 0.001px;
}
/* Items
 ========================================================================== */
/*
 * Reset whitespace hack
 */
.uk-breadcrumb > li {
  font-size: 1rem;
  vertical-align: top;
}
.uk-breadcrumb > li,
.uk-breadcrumb > li > a,
.uk-breadcrumb > li > span {
  display: inline-block;
}
.uk-breadcrumb > li:nth-child(n+2):before {
  content: "/";
  display: inline-block;
  margin: 0 8px;
}
/*
 * Disabled
 */
.uk-breadcrumb > li:not(.uk-active) > span {
  color: #999;
}
/* ========================================================================
   Component: Pagination
 ========================================================================== */
/*
 * 1. Remove default list style
 * 2. Center pagination by default
 * 3. Remove whitespace between child elements when using `inline-block`
 */
.uk-pagination {
  /* 1 */
  padding: 0;
  list-style: none;
  /* 2 */
  text-align: center;
  /* 3 */
  font-size: 0.001px;
}
/*
 * Micro clearfix
 * Needed if `uk-pagination-previous` or `uk-pagination-next` sub-objects are used
 */
.uk-pagination:before,
.uk-pagination:after {
  content: "";
  display: table;
}
.uk-pagination:after {
  clear: both;
}
/* Items
 ========================================================================== */
/*
 * 1. Reset whitespace hack
 * 2. Remove the gap at the bottom of it container
 */
.uk-pagination > li {
  display: inline-block;
  /* 1 */
  font-size: 1rem;
  /* 2 */
  vertical-align: top;
}
.uk-pagination > li:nth-child(n+2) {
  margin-left: 5px;
}
/*
 * 1. Makes pagination more robust against different box-sizing use
 * 2. Reset text-align to center if alignment modifier is used
 */
.uk-pagination > li > a,
.uk-pagination > li > span {
  display: inline-block;
  min-width: 16px;
  padding: 3px 5px;
  line-height: 20px;
  text-decoration: none;
  /* 1 */
  box-sizing: content-box;
  /* 2 */
  text-align: center;
  border-radius: 4px;
}
/*
 * Links
 */
.uk-pagination > li > a {
  background: #f7f7f7;
  color: #444;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-bottom-color: rgba(0, 0, 0, 0.3);
  background-origin: border-box;
  background-image: -webkit-linear-gradient(top, #fff, #eee);
  background-image: linear-gradient(to bottom, #fff, #eee);
  text-shadow: 0 1px 0 #fff;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-pagination > li > a:hover,
.uk-pagination > li > a:focus {
  background-color: #fafafa;
  color: #444;
  /* 2 */
  outline: none;
  background-image: none;
}
/* OnClick */
.uk-pagination > li > a:active {
  background-color: #f5f5f5;
  color: #444;
  border-color: rgba(0, 0, 0, 0.2);
  border-top-color: rgba(0, 0, 0, 0.3);
  background-image: none;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}
/*
 * Active
 */
.uk-pagination > .uk-active > span {
  background: #009dd8;
  color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-bottom-color: rgba(0, 0, 0, 0.4);
  background-origin: border-box;
  background-image: -webkit-linear-gradient(top, #00b4f5, #008dc5);
  background-image: linear-gradient(to bottom, #00b4f5, #008dc5);
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
}
/*
 * Disabled
 */
.uk-pagination > .uk-disabled > span {
  background-color: #fafafa;
  color: #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  text-shadow: 0 1px 0 #fff;
}
/* Previous and next navigation
 ========================================================================== */
.uk-pagination-previous {
  float: left;
}
.uk-pagination-next {
  float: right;
}
/* Alignment modifiers
 ========================================================================== */
.uk-pagination-left {
  text-align: left;
}
.uk-pagination-right {
  text-align: right;
}
/* ========================================================================
   Component: Tab
 ========================================================================== */
.uk-tab {
  margin: 0;
  padding: 0;
  list-style: none;
  border-bottom: 1px solid #ddd;
}
/*
 * Micro clearfix on the deepest container
 */
.uk-tab:before,
.uk-tab:after {
  content: "";
  display: table;
}
.uk-tab:after {
  clear: both;
}
/*
 * Items
 * 1. Create position context for dropdowns
 */
.uk-tab > li {
  margin-bottom: -1px;
  float: left;
  /* 1 */
  position: relative;
}
.uk-tab > li > a {
  display: block;
  padding: 8px 12px 8px 12px;
  border: 1px solid transparent;
  border-bottom-width: 0;
  color: #07D;
  text-decoration: none;
  border-radius: 4px 4px 0 0;
  text-shadow: 0 1px 0 #fff;
}
.uk-tab > li:nth-child(n+2) > a {
  margin-left: 5px;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Also apply if dropdown is opened
 * 3. Remove default focus style
 */
.uk-tab > li > a:hover,
.uk-tab > li > a:focus,
.uk-tab > li.uk-open > a {
  border-color: #ddd;
  background: #fafafa;
  color: #059;
  /* 2 */
  outline: none;
}
.uk-tab > li:not(.uk-active) > a:hover,
.uk-tab > li:not(.uk-active) > a:focus,
.uk-tab > li.uk-open:not(.uk-active) > a {
  margin-bottom: 1px;
  padding-bottom: 7px;
}
/* Active */
.uk-tab > li.uk-active > a {
  border-color: #ddd;
  border-bottom-color: transparent;
  background: #fff;
  color: #444;
}
/* Disabled */
.uk-tab > li.uk-disabled > a {
  color: #999;
  cursor: text;
}
.uk-tab > li.uk-disabled > a:hover,
.uk-tab > li.uk-disabled > a:focus,
.uk-tab > li.uk-disabled.uk-active > a {
  background: none;
  border-color: transparent;
}
/* Modifier: 'tab-flip'
 ========================================================================== */
.uk-tab-flip > li {
  float: right;
}
.uk-tab-flip > li:nth-child(n+2) > a {
  margin-left: 0;
  margin-right: 5px;
}
/* Modifier: 'tab-responsive'
 ========================================================================== */
.uk-tab > li.uk-tab-responsive > a {
  margin-left: 0;
  margin-right: 0;
}
/*
 * Icon
 */
.uk-tab-responsive > a:before {
  content: "\\f0c9\\00a0";
  font-family: FontAwesome;
}
/* Modifier: 'tab-center'
 ========================================================================== */
.uk-tab-center {
  border-bottom: 1px solid #ddd;
}
.uk-tab-center-bottom {
  border-bottom: none;
  border-top: 1px solid #ddd;
}
.uk-tab-center:before,
.uk-tab-center:after {
  content: "";
  display: table;
}
.uk-tab-center:after {
  clear: both;
}
/*
 * 1. Using `right` to prevent vertical scrollbar caused by centering if to many tabs
 */
.uk-tab-center .uk-tab {
  position: relative;
  right: 50%;
  border: none;
  float: right;
}
.uk-tab-center .uk-tab > li {
  position: relative;
  right: -50%;
}
.uk-tab-center .uk-tab > li > a {
  text-align: center;
}
/* Modifier: 'tab-bottom'
 ========================================================================== */
.uk-tab-bottom {
  border-top: 1px solid #ddd;
  border-bottom: none;
}
.uk-tab-bottom > li {
  margin-top: -1px;
  margin-bottom: 0;
}
.uk-tab-bottom > li > a {
  padding-top: 8px;
  padding-bottom: 8px;
  border-bottom-width: 1px;
  border-top-width: 0;
}
.uk-tab-bottom > li:not(.uk-active) > a:hover,
.uk-tab-bottom > li:not(.uk-active) > a:focus,
.uk-tab-bottom > li.uk-open:not(.uk-active) > a {
  margin-bottom: 0;
  margin-top: 1px;
  padding-bottom: 8px;
  padding-top: 7px;
}
.uk-tab-bottom > li.uk-active > a {
  border-top-color: transparent;
  border-bottom-color: #ddd;
}
/* Modifier: 'tab-grid'
 ========================================================================== */
/*
 * 1. Create position context to prevent hidden border because of negative `z-index`
 */
.uk-tab-grid {
  margin-left: -5px;
  border-bottom: none;
  /* 1 */
  position: relative;
  z-index: 0;
}
.uk-tab-grid:before {
  display: block;
  position: absolute;
  left: 5px;
  right: 0;
  bottom: -1px;
  border-top: 1px solid #ddd;
  /* 1 */
  z-index: -1;
}
.uk-tab-grid > li:first-child > a {
  margin-left: 5px;
}
.uk-tab-grid > li > a {
  text-align: center;
}
/*
 * If `uk-tab-bottom`
 */
.uk-tab-grid.uk-tab-bottom {
  border-top: none;
}
.uk-tab-grid.uk-tab-bottom:before {
  top: -1px;
  bottom: auto;
}
/* Modifier: 'tab-left', 'tab-right'
 ========================================================================== */
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-tab-left,
  .uk-tab-right {
    border-bottom: none;
  }
  .uk-tab-left > li,
  .uk-tab-right > li {
    margin-bottom: 0;
    float: none;
  }
  .uk-tab-left > li > a,
  .uk-tab-right > li > a {
    padding-top: 8px;
    padding-bottom: 8px;
  }
  .uk-tab-left > li:nth-child(n+2) > a,
  .uk-tab-right > li:nth-child(n+2) > a {
    margin-left: 0;
    margin-top: 5px;
  }
  .uk-tab-left > li.uk-active > a,
  .uk-tab-right > li.uk-active > a {
    border-color: #ddd;
  }
  /*
     * Modifier: 'tab-left'
     */
  .uk-tab-left {
    border-right: 1px solid #ddd;
  }
  .uk-tab-left > li {
    margin-right: -1px;
  }
  .uk-tab-left > li > a {
    border-bottom-width: 1px;
    border-right-width: 0;
  }
  .uk-tab-left > li:not(.uk-active) > a:hover,
  .uk-tab-left > li:not(.uk-active) > a:focus {
    margin-bottom: 0;
    margin-right: 1px;
    padding-bottom: 8px;
    padding-right: 11px;
  }
  .uk-tab-left > li.uk-active > a {
    border-right-color: transparent;
  }
  /*
     * Modifier: 'tab-right'
     */
  .uk-tab-right {
    border-left: 1px solid #ddd;
  }
  .uk-tab-right > li {
    margin-left: -1px;
  }
  .uk-tab-right > li > a {
    border-bottom-width: 1px;
    border-left-width: 0;
  }
  .uk-tab-right > li:not(.uk-active) > a:hover,
  .uk-tab-right > li:not(.uk-active) > a:focus {
    margin-bottom: 0;
    margin-left: 1px;
    padding-bottom: 8px;
    padding-left: 11px;
  }
  .uk-tab-right > li.uk-active > a {
    border-left-color: transparent;
  }
}
/* Modifier: `uk-tab-bottom'
     ========================================================================== */
.uk-tab-bottom > li > a {
  border-radius: 0 0 4px 4px;
}
/* Modifier: `uk-tab-left', `uk-tab-right'
    ========================================================================== */
/* Tablet and bigger */
@media (min-width: 768px) {
  /*
         * Modifier: `uk-tab-left'
         */
  .uk-tab-left > li > a {
    border-radius: 4px 0 0 4px;
  }
  /*
         * Modifier: `uk-tab-right'
         */
  .uk-tab-right > li > a {
    border-radius: 0 4px 4px 0;
  }
}
/* ========================================================================
   Component: Thumbnav
 ========================================================================== */
/*
 * 1. Gutter
 * 2. Remove default list style
 */
.uk-thumbnav {
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -ms-flex-wrap: wrap;
  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;
  /* 1 */
  margin-left: -10px;
  margin-top: -10px;
  /* 2 */
  padding: 0;
  list-style: none;
}
/*
 * 1. Space is allocated solely based on content dimensions
 * 2. Horizontal gutter is using `padding` so `uk-width-*` classes can be applied
 */
.uk-thumbnav > * {
  /* 1 */
  -ms-flex: none;
  -webkit-flex: none;
  flex: none;
  /* 2 */
  padding-left: 10px;
  margin-top: 10px;
}
/*
 * DEPRECATED IE9 Support
 */
.uk-thumbnav:before,
.uk-thumbnav:after {
  content: "";
  display: block;
  overflow: hidden;
}
.uk-thumbnav:after {
  clear: both;
}
.uk-thumbnav > * {
  float: left;
}
/* Items
 ========================================================================== */
.uk-thumbnav > * > * {
  display: block;
  background: #fff;
}
.uk-thumbnav > * > * > img {
  opacity: 0.7;
  -webkit-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
/*
 * Hover
 */
.uk-thumbnav > * > :hover > img,
.uk-thumbnav > * > :focus > img {
  opacity: 1;
}
/*
 * Active
 */
.uk-thumbnav > .uk-active > * > img {
  opacity: 1;
}
/* ========================================================================
   Component: List
 ========================================================================== */
.uk-list {
  padding: 0;
  list-style: none;
}
/*
 * Micro clearfix to make list more robust
 */
.uk-list > li:before,
.uk-list > li:after {
  content: "";
  display: table;
}
.uk-list > li:after {
  clear: both;
}
/*
 * Remove margin from the last-child
 */
.uk-list > li > :last-child {
  margin-bottom: 0;
}
/*
 * Nested lists
 */
.uk-list ul {
  margin: 0;
  padding-left: 20px;
  list-style: none;
}
/* Modifier: `uk-list-line`
 ========================================================================== */
.uk-list-line > li:nth-child(n+2) {
  margin-top: 5px;
  padding-top: 5px;
  border-top: 1px solid #ddd;
}
/* Modifier: `uk-list-striped`
 ========================================================================== */
.uk-list-striped > li {
  padding: 5px 5px;
  border-bottom: 1px solid #ddd;
}
.uk-list-striped > li:nth-of-type(odd) {
  background: #fafafa;
}
/* Modifier: `uk-list-space`
 ========================================================================== */
.uk-list-space > li:nth-child(n+2) {
  margin-top: 10px;
}
.uk-list-striped > li:first-child {
  border-top: 1px solid #ddd;
}
/* ========================================================================
   Component: Description list
 ========================================================================== */
/* Modifier: `uk-description-list-horizontal`
 ========================================================================== */
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-description-list-horizontal {
    overflow: hidden;
  }
  .uk-description-list-horizontal > dt {
    width: 160px;
    float: left;
    clear: both;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .uk-description-list-horizontal > dd {
    margin-left: 180px;
  }
}
/* Modifier: `uk-description-list-line`
 ========================================================================== */
.uk-description-list-line > dt {
  font-weight: normal;
}
.uk-description-list-line > dt:nth-child(n+2) {
  margin-top: 5px;
  padding-top: 5px;
  border-top: 1px solid #ddd;
}
.uk-description-list-line > dd {
  color: #999;
}
/* ========================================================================
   Component: Table
 ========================================================================== */
/*
 * 1. Remove most spacing between table cells.
 * 2. Block element behavior
 * 3. Style
 */
.uk-table {
  /* 1 */
  border-collapse: collapse;
  border-spacing: 0;
  /* 2 */
  width: 100%;
  /* 3 */
  margin-bottom: 15px;
}
/*
 * Add margin if adjacent element
 */
* + .uk-table {
  margin-top: 15px;
}
.uk-table th,
.uk-table td {
  padding: 8px 8px;
  border-bottom: 1px solid #ddd;
}
/*
 * Set alignment
 */
.uk-table th {
  text-align: left;
}
.uk-table td {
  vertical-align: top;
}
.uk-table thead th {
  vertical-align: bottom;
}
/*
 * Caption and footer
 */
.uk-table caption,
.uk-table tfoot {
  font-size: 12px;
  font-style: italic;
}
.uk-table caption {
  text-align: left;
  color: #999;
}
/*
 * Active State
 */
.uk-table tbody tr.uk-active {
  background: #f0f0f0;
}
/* Sub-modifier: `uk-table-middle`
 ========================================================================== */
.uk-table-middle,
.uk-table-middle td {
  vertical-align: middle !important;
}
/* Modifier: `uk-table-striped`
 ========================================================================== */
.uk-table-striped tbody tr:nth-of-type(odd) {
  background: #fafafa;
}
/* Modifier: `uk-table-condensed`
 ========================================================================== */
.uk-table-condensed td {
  padding: 4px 8px;
}
/* Modifier: `uk-table-hover`
 ========================================================================== */
.uk-table-hover tbody tr:hover {
  background: #f0f0f0;
}
/* ========================================================================
   Component: Form
 ========================================================================== */
/*
 * 1. Define consistent box sizing.
 *    Default is `content-box` with following exceptions set to `border-box`
 *    `button`, `select`, `input[type="checkbox"]` and `input[type="radio"]`
 *    `input[type="search"]` in Chrome, Safari and Opera
 *    `input[type="color"]` in Firefox
 * 2. Address margins set differently in Firefox/IE and Chrome/Safari/Opera.
 * 3. Remove `border-radius` in iOS.
 * 4. Correct `font` properties and `color` not being inherited.
 */
.uk-form input,
.uk-form select,
.uk-form textarea {
  /* 1 */
  box-sizing: border-box;
  /* 2 */
  margin: 0;
  /* 3 */
  border-radius: 0;
  /* 4 */
  font: inherit;
  color: inherit;
}
/*
 * Address inconsistent `text-transform` inheritance which is only inherit in Firefox
 */
.uk-form select {
  text-transform: none;
}
/*
 * 1. Correct `font` properties not being inherited.
 * 2. Don't inherit the `font-weight` and use `bold` instead.
 * NOTE: Both declarations don't work in Chrome, Safari and Opera.
 */
.uk-form optgroup {
  /* 1 */
  font: inherit;
  /* 2 */
  font-weight: bold;
}
/*
 * Removes inner padding and border in Firefox 4+.
 */
.uk-form input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
/*
 * Removes excess padding in IE 8/9/10.
 */
.uk-form input[type="checkbox"],
.uk-form input[type="radio"] {
  padding: 0;
}
/*
 * Improves consistency of cursor style for clickable elements
 */
.uk-form input[type="checkbox"]:not(:disabled),
.uk-form input[type="radio"]:not(:disabled) {
  cursor: pointer;
}
/*
 * Remove default style in iOS.
 */
.uk-form textarea,
.uk-form input:not([type]),
.uk-form input[type="text"],
.uk-form input[type="password"],
.uk-form input[type="email"],
.uk-form input[type="url"],
.uk-form input[type="search"],
.uk-form input[type="tel"],
.uk-form input[type="number"],
.uk-form input[type="datetime"] {
  -webkit-appearance: none;
}
/*
 * Remove inner padding and search cancel button in Chrome, Safari and Opera on OS X.
 */
.uk-form input[type="search"]::-webkit-search-cancel-button,
.uk-form input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
/*
 * Fix the cursor style for Chrome's increment/decrement buttons. For certain
 * `font-size` values of the `input`, it causes the cursor style of the
 * decrement button to change from `default` to `text`.
 */
.uk-form input[type="number"]::-webkit-inner-spin-button,
.uk-form input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
/*
 * Define consistent border, margin, and padding.
 */
.uk-form fieldset {
  border: none;
  margin: 0;
  padding: 0;
}
/*
 * 1. Remove default vertical scrollbar in IE 8/9/10/11.
 * 2. Improve readability and alignment in all browsers.
 */
.uk-form textarea {
  /* 1 */
  overflow: auto;
  /* 2 */
  vertical-align: top;
}
/*
 * Removes placeholder transparency in Firefox.
 */
.uk-form ::-moz-placeholder {
  opacity: 1;
}
/*
 * Removes `box-shadow` for invalid controls in Firefox.
 */
.uk-form :invalid {
  box-shadow: none;
}
/*
 * Vertical alignment
 */
.uk-form input:not([type="radio"]):not([type="checkbox"]),
.uk-form select {
  vertical-align: middle;
}
/* Style
 ========================================================================== */
/*
 * Remove margin from the last-child
 */
.uk-form > :last-child {
  margin-bottom: 0;
}
/*
 * Controls
 * Except for `range`, `radio`, `checkbox`, `file`, `submit`, `reset`, `button` and `image`
 * 1. Must be `height` because `min-height` is not working in OSX
 * 2. Responsiveness: Sets a maximum width relative to the parent to scale on narrower viewports
 * 3. Vertical `padding` needed for `select` elements in Firefox
 * 4. Style
 */
.uk-form select,
.uk-form textarea,
.uk-form input:not([type]),
.uk-form input[type="text"],
.uk-form input[type="password"],
.uk-form input[type="datetime"],
.uk-form input[type="datetime-local"],
.uk-form input[type="date"],
.uk-form input[type="month"],
.uk-form input[type="time"],
.uk-form input[type="week"],
.uk-form input[type="number"],
.uk-form input[type="email"],
.uk-form input[type="url"],
.uk-form input[type="search"],
.uk-form input[type="tel"],
.uk-form input[type="color"] {
  /* 1 */
  height: 30px;
  /* 2 */
  max-width: 100%;
  /* 3 */
  padding: 4px 6px;
  /* 4 */
  border: 1px solid #ddd;
  background: #fff;
  color: #444;
  -webkit-transition: all 0.2s linear;
  -webkit-transition-property: border, background, color, box-shadow, padding;
  transition: all 0.2s linear;
  transition-property: border, background, color, box-shadow, padding;
  border-radius: 4px;
}
.uk-form select:focus,
.uk-form textarea:focus,
.uk-form input:not([type]):focus,
.uk-form input[type="text"]:focus,
.uk-form input[type="password"]:focus,
.uk-form input[type="datetime"]:focus,
.uk-form input[type="datetime-local"]:focus,
.uk-form input[type="date"]:focus,
.uk-form input[type="month"]:focus,
.uk-form input[type="time"]:focus,
.uk-form input[type="week"]:focus,
.uk-form input[type="number"]:focus,
.uk-form input[type="email"]:focus,
.uk-form input[type="url"]:focus,
.uk-form input[type="search"]:focus,
.uk-form input[type="tel"]:focus,
.uk-form input[type="color"]:focus {
  border-color: #99baca;
  outline: 0;
  background: #f5fbfe;
  color: #444;
}
.uk-form select:disabled,
.uk-form textarea:disabled,
.uk-form input:not([type]):disabled,
.uk-form input[type="text"]:disabled,
.uk-form input[type="password"]:disabled,
.uk-form input[type="datetime"]:disabled,
.uk-form input[type="datetime-local"]:disabled,
.uk-form input[type="date"]:disabled,
.uk-form input[type="month"]:disabled,
.uk-form input[type="time"]:disabled,
.uk-form input[type="week"]:disabled,
.uk-form input[type="number"]:disabled,
.uk-form input[type="email"]:disabled,
.uk-form input[type="url"]:disabled,
.uk-form input[type="search"]:disabled,
.uk-form input[type="tel"]:disabled,
.uk-form input[type="color"]:disabled {
  border-color: #ddd;
  background-color: #fafafa;
  color: #999;
}
/*
 * Placeholder
 */
.uk-form :-ms-input-placeholder {
  color: #999 !important;
}
.uk-form ::-moz-placeholder {
  color: #999;
}
.uk-form ::-webkit-input-placeholder {
  color: #999;
}
.uk-form :disabled:-ms-input-placeholder {
  color: #999 !important;
}
.uk-form :disabled::-moz-placeholder {
  color: #999;
}
.uk-form :disabled::-webkit-input-placeholder {
  color: #999;
}
/*
 * Legend
 * 1. Behave like block element
 * 2. Correct `color` not being inherited in IE 8/9/10/11.
 * 3. Remove padding
 * 4. `margin-bottom` is not working in Safari and Opera.
 *    Using `padding` and :after instead to create the border
 * 5. Style
 */
.uk-form legend {
  /* 1 */
  width: 100%;
  /* 2 */
  border: 0;
  /* 3 */
  padding: 0;
  /* 4 */
  padding-bottom: 15px;
  /* 5 */
  font-size: 18px;
  line-height: 30px;
}
/*
 * 1. Fixes IE9
 */
.uk-form legend:after {
  content: "";
  display: block;
  border-bottom: 1px solid #ddd;
  /* 1 */
  width: 100%;
}
/* Size modifiers
 * Higher specificity needed to override defaults
 ========================================================================== */
select.uk-form-small,
textarea.uk-form-small,
input[type].uk-form-small,
input:not([type]).uk-form-small {
  height: 25px;
  padding: 3px 3px;
  font-size: 12px;
}
select.uk-form-large,
textarea.uk-form-large,
input[type].uk-form-large,
input:not([type]).uk-form-large {
  height: 40px;
  padding: 8px 6px;
  font-size: 16px;
}
/* Reset height
 * Must be after size modifiers
 ========================================================================== */
.uk-form textarea,
.uk-form select[multiple],
.uk-form select[size] {
  height: auto;
}
/* Validation states
 * Using !important to keep the selector simple
 ========================================================================== */
/*
 * Error state
 */
.uk-form-danger {
  border-color: #dc8d99 !important;
  background: #fff7f8 !important;
  color: #d85030 !important;
}
/*
 * Success state
 */
.uk-form-success {
  border-color: #8ec73b !important;
  background: #fafff2 !important;
  color: #659f13 !important;
}
/* Style modifiers
 * Using !important to keep the selector simple
 ========================================================================== */
/*
 * Blank form
 */
.uk-form-blank {
  border-color: transparent !important;
  border-style: dashed !important;
  background: none !important;
}
.uk-form-blank:focus {
  border-color: #ddd !important;
}
/* Size sub-modifiers
 ========================================================================== */
/*
 * Fixed widths
 * Different widths for mini sized `input` and `select` elements
 */
input.uk-form-width-mini {
  width: 40px;
}
select.uk-form-width-mini {
  width: 65px;
}
.uk-form-width-small {
  width: 130px;
}
.uk-form-width-medium {
  width: 200px;
}
.uk-form-width-large {
  width: 500px;
}
/* Sub-objects: `uk-form-row`
 * Groups labels and controls in rows
 ========================================================================== */
/*
 * Micro clearfix
 * Needed for `uk-form-horizontal` modifier
 */
.uk-form-row:before,
.uk-form-row:after {
  content: "";
  display: table;
}
.uk-form-row:after {
  clear: both;
}
/*
 * Vertical gutter
 */
.uk-form-row + .uk-form-row {
  margin-top: 15px;
}
/* Help text
 * Sub-object: `uk-form-help-inline`, `uk-form-help-block`
 ========================================================================== */
.uk-form-help-inline {
  display: inline-block;
  margin: 0 0 0 10px;
}
.uk-form-help-block {
  margin: 5px 0 0 0;
}
/* Controls content
 * Sub-object: `uk-form-controls`, `uk-form-controls-condensed`
 ========================================================================== */
/*
 * Remove margins
 */
.uk-form-controls > :first-child {
  margin-top: 0;
}
.uk-form-controls > :last-child {
  margin-bottom: 0;
}
/*
 * Group controls and text into blocks with a small spacing between blocks
 */
.uk-form-controls-condensed {
  margin: 5px 0;
}
/* Modifier: `uk-form-stacked`
 * Requires sub-object: `uk-form-label`
 ========================================================================== */
.uk-form-stacked .uk-form-label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}
/* Modifier: `uk-form-horizontal`
 * Requires sub-objects: `uk-form-label`, `uk-form-controls`
 ========================================================================== */
/* Tablet portrait and smaller */
@media (max-width: 959px) {
  /* Behave like `uk-form-stacked` */
  .uk-form-horizontal .uk-form-label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
}
/* Desktop and bigger */
@media (min-width: 960px) {
  .uk-form-horizontal .uk-form-label {
    width: 200px;
    margin-top: 5px;
    float: left;
  }
  .uk-form-horizontal .uk-form-controls {
    margin-left: 215px;
  }
  /* Better vertical alignment if controls are checkboxes and radio buttons with text */
  .uk-form-horizontal .uk-form-controls-text {
    padding-top: 5px;
  }
}
/* Sub-object: `uk-form-icon`
 ========================================================================== */
/*
 * 1. Container width fits its content
 * 2. Create position context
 * 3. Prevent `inline-block` consequences
 */
.uk-form-icon {
  /* 1 */
  display: inline-block;
  /* 2 */
  position: relative;
  /* 3 */
  max-width: 100%;
}
/*
 * 1. Make form element clickable through icon
 */
.uk-form-icon > [class*='uk-icon-'] {
  position: absolute;
  top: 50%;
  width: 30px;
  margin-top: -7px;
  font-size: 14px;
  color: #999;
  text-align: center;
  /* 1 */
  pointer-events: none;
}
.uk-form-icon:not(.uk-form-icon-flip) > input {
  padding-left: 30px !important;
}
/*
 * Sub-modifier: `uk-form-icon-flip`
 */
.uk-form-icon-flip > [class*='uk-icon-'] {
  right: 0;
}
.uk-form-icon-flip > input {
  padding-right: 30px !important;
}
/* ========================================================================
   Component: Button
 ========================================================================== */
/*
 * Removes inner padding and border in Firefox 4+.
 */
.uk-button::-moz-focus-inner {
  border: 0;
  padding: 0;
}
/*
 * 1. Correct inability to style clickable `input` types in iOS.
 * 2. Remove margins in Chrome, Safari and Opera.
 * 3. Remove borders for `button`.
 * 4. Address `overflow` set to `hidden` in IE 8/9/10/11.
 * 5. Correct `font` properties and `color` not being inherited for `button`.
 * 6. Address inconsistent `text-transform` inheritance which is only inherit in Firefox and IE
 * 7. Style
 * 8. `line-height` is used to create a height
 * 9. `min-height` is necessary for `input` elements in Firefox and Opera because `line-height` is not working.
 * 10. Reset button group whitespace hack
 * 11. Required for `a`.
 */
.uk-button {
  /* 1 */
  -webkit-appearance: none;
  /* 2 */
  margin: 0;
  /* 3 */
  border: none;
  /* 4 */
  overflow: visible;
  /* 5 */
  font: inherit;
  color: #444;
  /* 6 */
  text-transform: none;
  /* 7 */
  display: inline-block;
  box-sizing: border-box;
  padding: 0 12px;
  background: #f7f7f7;
  vertical-align: middle;
  /* 8 */
  line-height: 28px;
  /* 9 */
  min-height: 30px;
  /* 10 */
  font-size: 1rem;
  /* 11 */
  text-decoration: none;
  text-align: center;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-bottom-color: rgba(0, 0, 0, 0.3);
  background-origin: border-box;
  background-image: -webkit-linear-gradient(top, #fff, #eee);
  background-image: linear-gradient(to bottom, #fff, #eee);
  border-radius: 4px;
  text-shadow: 0 1px 0 #fff;
}
.uk-button:not(:disabled) {
  cursor: pointer;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 * 3. Required for `a` elements
 */
.uk-button:hover,
.uk-button:focus {
  background-color: #fafafa;
  color: #444;
  /* 2 */
  outline: none;
  /* 3 */
  text-decoration: none;
  background-image: none;
}
/* Active */
.uk-button:active,
.uk-button.uk-active {
  background-color: #f5f5f5;
  color: #444;
  border-color: rgba(0, 0, 0, 0.2);
  border-top-color: rgba(0, 0, 0, 0.3);
  background-image: none;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}
/* Color modifiers
 ========================================================================== */
/*
 * Modifier: `uk-button-primary`
 */
.uk-button-primary {
  background-color: #009dd8;
  color: #fff;
  background-image: -webkit-linear-gradient(top, #00b4f5, #008dc5);
  background-image: linear-gradient(to bottom, #00b4f5, #008dc5);
  border-color: rgba(0, 0, 0, 0.2);
  border-bottom-color: rgba(0, 0, 0, 0.4);
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
}
/* Hover */
.uk-button-primary:hover,
.uk-button-primary:focus {
  background-color: #00aff2;
  color: #fff;
  background-image: none;
}
/* Active */
.uk-button-primary:active,
.uk-button-primary.uk-active {
  background-color: #008abf;
  color: #fff;
  background-image: none;
  border-color: rgba(0, 0, 0, 0.2);
  border-top-color: rgba(0, 0, 0, 0.4);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}
/*
 * Modifier: `uk-button-success`
 */
.uk-button-success {
  background-color: #82bb42;
  color: #fff;
  background-image: -webkit-linear-gradient(top, #9fd256, #6fac34);
  background-image: linear-gradient(to bottom, #9fd256, #6fac34);
  border-color: rgba(0, 0, 0, 0.2);
  border-bottom-color: rgba(0, 0, 0, 0.4);
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
}
/* Hover */
.uk-button-success:hover,
.uk-button-success:focus {
  background-color: #8fce48;
  color: #fff;
  background-image: none;
}
/* Active */
.uk-button-success:active,
.uk-button-success.uk-active {
  background-color: #76b430;
  color: #fff;
  background-image: none;
  border-color: rgba(0, 0, 0, 0.2);
  border-top-color: rgba(0, 0, 0, 0.4);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}
/*
 * Modifier: `uk-button-danger`
 */
.uk-button-danger {
  background-color: #d32c46;
  color: #fff;
  background-image: -webkit-linear-gradient(top, #ee465a, #c11a39);
  background-image: linear-gradient(to bottom, #ee465a, #c11a39);
  border-color: rgba(0, 0, 0, 0.2);
  border-bottom-color: rgba(0, 0, 0, 0.4);
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
}
/* Hover */
.uk-button-danger:hover,
.uk-button-danger:focus {
  background-color: #e33551;
  color: #fff;
  background-image: none;
}
/* Active */
.uk-button-danger:active,
.uk-button-danger.uk-active {
  background-color: #c91c37;
  color: #fff;
  background-image: none;
  border-color: rgba(0, 0, 0, 0.2);
  border-top-color: rgba(0, 0, 0, 0.4);
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}
/* Disabled state
 * Overrides also the color modifiers
 ========================================================================== */
/* Equal for all button types */
.uk-button:disabled {
  background-color: #fafafa;
  color: #999;
  border-color: rgba(0, 0, 0, 0.2);
  background-image: none;
  box-shadow: none;
  text-shadow: 0 1px 0 #fff;
}
/* Modifier: `uk-button-link`
 ========================================================================== */
/* Reset */
.uk-button-link,
.uk-button-link:hover,
.uk-button-link:focus,
.uk-button-link:active,
.uk-button-link.uk-active,
.uk-button-link:disabled {
  border-color: transparent;
  background: none;
  box-shadow: none;
  text-shadow: none;
}
/* Color */
.uk-button-link {
  color: #07D;
}
.uk-button-link:hover,
.uk-button-link:focus,
.uk-button-link:active,
.uk-button-link.uk-active {
  color: #059;
  text-decoration: underline;
}
.uk-button-link:disabled {
  color: #999;
}
/* Focus */
.uk-button-link:focus {
  outline: 1px dotted;
}
/* Size modifiers
 ========================================================================== */
.uk-button-mini {
  min-height: 20px;
  padding: 0 6px;
  line-height: 18px;
  font-size: 11px;
}
.uk-button-small {
  min-height: 25px;
  padding: 0 10px;
  line-height: 23px;
  font-size: 12px;
}
.uk-button-large {
  min-height: 40px;
  padding: 0 15px;
  line-height: 38px;
  font-size: 16px;
  border-radius: 5px;
}
/* Sub-object `uk-button-group`
 ========================================================================== */
/*
 * 1. Behave like buttons
 * 2. Create position context for dropdowns
 * 3. Remove whitespace between child elements when using `inline-block`
 * 4. Prevent buttons from wrapping
 * 5. Remove whitespace between child elements when using `inline-block`
 */
.uk-button-group {
  /* 1 */
  display: inline-block;
  vertical-align: middle;
  /* 2 */
  position: relative;
  /* 3 */
  font-size: 0.001px;
  /* 4 */
  white-space: nowrap;
}
.uk-button-group > * {
  display: inline-block;
}
/* 5 */
.uk-button-group .uk-button {
  vertical-align: top;
}
/* Sub-object: `uk-button-dropdown`
 ========================================================================== */
/*
 * 1. Behave like buttons
 * 2. Create position context for dropdowns
 */
.uk-button-dropdown {
  /* 1 */
  display: inline-block;
  vertical-align: middle;
  /* 2 */
  position: relative;
}
/* Sub-object `uk-button-group`
     ========================================================================== */
/*
     * Reset border-radius
     */
.uk-button-group > .uk-button:not(:first-child):not(:last-child),
.uk-button-group > div:not(:first-child):not(:last-child) .uk-button {
  border-radius: 0;
}
.uk-button-group > .uk-button:first-child,
.uk-button-group > div:first-child .uk-button {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}
.uk-button-group > .uk-button:last-child,
.uk-button-group > div:last-child .uk-button {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}
/*
     * Collapse border
     */
.uk-button-group > .uk-button:nth-child(n+2),
.uk-button-group > div:nth-child(n+2) .uk-button {
  margin-left: -1px;
}
/*
     * Create position context to superimpose the successor elements border
     * Known issue: If you use an `a` element as button and an icon inside,
     * the active state will not work if you click the icon inside the button
     * Workaround: Just use a `button` or `input` element as button
     */
.uk-button-group .uk-button:hover,
.uk-button-group .uk-button:active,
.uk-button-group .uk-button.uk-active {
  position: relative;
}
/* ========================================================================
   Component: Icon
 ========================================================================== */
@font-face {
  font-family: 'FontAwesome';
  src: url("../fonts/fontawesome-webfont.woff2") format('woff2'), url("../fonts/fontawesome-webfont.woff") format("woff"), url("../fonts/fontawesome-webfont.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
/*
 * 1. Allow margin
 * 2. Prevent inherit font style
 * 4. Correct line-height
 * 5. Better font rendering
 * 6. Remove `text-decoration` for anchors
 */
[class*='uk-icon-'] {
  font-family: FontAwesome;
  /* 1 */
  display: inline-block;
  /* 2 */
  font-weight: normal;
  font-style: normal;
  /* 4 */
  line-height: 1;
  /* 5 */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* 6 */
[class*='uk-icon-'],
[class*='uk-icon-']:hover,
[class*='uk-icon-']:focus {
  text-decoration: none;
}
/* Size modifiers
 ========================================================================== */
.uk-icon-small {
  font-size: 150%;
  vertical-align: -10%;
}
.uk-icon-medium {
  font-size: 200%;
  vertical-align: -16%;
}
.uk-icon-large {
  font-size: 250%;
  vertical-align: -22%;
}
/* Modifier: `uk-icon-justify`
 ========================================================================== */
.uk-icon-justify {
  width: 1em;
  text-align: center;
}
/* Modifier: `uk-icon-spin`
 ========================================================================== */
.uk-icon-spin {
  display: inline-block;
  -webkit-animation: uk-rotate 2s infinite linear;
  animation: uk-rotate 2s infinite linear;
}
/* Modifier: `uk-icon-hover`
 ========================================================================== */
.uk-icon-hover {
  color: #999;
}
/*
 * Hover
 */
.uk-icon-hover:hover {
  color: #444;
}
/* Modifier: `uk-icon-button`
 ========================================================================== */
.uk-icon-button {
  box-sizing: border-box;
  display: inline-block;
  width: 35px;
  height: 35px;
  border-radius: 100%;
  background: #f7f7f7;
  line-height: 35px;
  color: #444;
  font-size: 18px;
  text-align: center;
  border: 1px solid #ccc;
  border-bottom-color: #bbb;
  background-origin: border-box;
  background-image: -webkit-linear-gradient(top, #fff, #eee);
  background-image: linear-gradient(to bottom, #fff, #eee);
  text-shadow: 0 1px 0 #fff;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 */
.uk-icon-button:hover,
.uk-icon-button:focus {
  background-color: #fafafa;
  color: #444;
  /* 2 */
  outline: none;
  background-image: none;
}
/* Active */
.uk-icon-button:active {
  background-color: #f5f5f5;
  color: #444;
  border-color: #ccc;
  border-top-color: #bbb;
  background-image: none;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}
/* Icon mapping
 ========================================================================== */
.uk-icon-glass:before {
  content: "\\f000";
}
.uk-icon-music:before {
  content: "\\f001";
}
.uk-icon-search:before {
  content: "\\f002";
}
.uk-icon-envelope-o:before {
  content: "\\f003";
}
.uk-icon-heart:before {
  content: "\\f004";
}
.uk-icon-star:before {
  content: "\\f005";
}
.uk-icon-star-o:before {
  content: "\\f006";
}
.uk-icon-user:before {
  content: "\\f007";
}
.uk-icon-film:before {
  content: "\\f008";
}
.uk-icon-th-large:before {
  content: "\\f009";
}
.uk-icon-th:before {
  content: "\\f00a";
}
.uk-icon-th-list:before {
  content: "\\f00b";
}
.uk-icon-check:before {
  content: "\\f00c";
}
.uk-icon-remove:before,
.uk-icon-close:before,
.uk-icon-times:before {
  content: "\\f00d";
}
.uk-icon-search-plus:before {
  content: "\\f00e";
}
.uk-icon-search-minus:before {
  content: "\\f010";
}
.uk-icon-power-off:before {
  content: "\\f011";
}
.uk-icon-signal:before {
  content: "\\f012";
}
.uk-icon-gear:before,
.uk-icon-cog:before {
  content: "\\f013";
}
.uk-icon-trash-o:before {
  content: "\\f014";
}
.uk-icon-home:before {
  content: "\\f015";
}
.uk-icon-file-o:before {
  content: "\\f016";
}
.uk-icon-clock-o:before {
  content: "\\f017";
}
.uk-icon-road:before {
  content: "\\f018";
}
.uk-icon-download:before {
  content: "\\f019";
}
.uk-icon-arrow-circle-o-down:before {
  content: "\\f01a";
}
.uk-icon-arrow-circle-o-up:before {
  content: "\\f01b";
}
.uk-icon-inbox:before {
  content: "\\f01c";
}
.uk-icon-play-circle-o:before {
  content: "\\f01d";
}
.uk-icon-rotate-right:before,
.uk-icon-repeat:before {
  content: "\\f01e";
}
.uk-icon-refresh:before {
  content: "\\f021";
}
.uk-icon-list-alt:before {
  content: "\\f022";
}
.uk-icon-lock:before {
  content: "\\f023";
}
.uk-icon-flag:before {
  content: "\\f024";
}
.uk-icon-headphones:before {
  content: "\\f025";
}
.uk-icon-volume-off:before {
  content: "\\f026";
}
.uk-icon-volume-down:before {
  content: "\\f027";
}
.uk-icon-volume-up:before {
  content: "\\f028";
}
.uk-icon-qrcode:before {
  content: "\\f029";
}
.uk-icon-barcode:before {
  content: "\\f02a";
}
.uk-icon-tag:before {
  content: "\\f02b";
}
.uk-icon-tags:before {
  content: "\\f02c";
}
.uk-icon-book:before {
  content: "\\f02d";
}
.uk-icon-bookmark:before {
  content: "\\f02e";
}
.uk-icon-print:before {
  content: "\\f02f";
}
.uk-icon-camera:before {
  content: "\\f030";
}
.uk-icon-font:before {
  content: "\\f031";
}
.uk-icon-bold:before {
  content: "\\f032";
}
.uk-icon-italic:before {
  content: "\\f033";
}
.uk-icon-text-height:before {
  content: "\\f034";
}
.uk-icon-text-width:before {
  content: "\\f035";
}
.uk-icon-align-left:before {
  content: "\\f036";
}
.uk-icon-align-center:before {
  content: "\\f037";
}
.uk-icon-align-right:before {
  content: "\\f038";
}
.uk-icon-align-justify:before {
  content: "\\f039";
}
.uk-icon-list:before {
  content: "\\f03a";
}
.uk-icon-dedent:before,
.uk-icon-outdent:before {
  content: "\\f03b";
}
.uk-icon-indent:before {
  content: "\\f03c";
}
.uk-icon-video-camera:before {
  content: "\\f03d";
}
.uk-icon-photo:before,
.uk-icon-image:before,
.uk-icon-picture-o:before {
  content: "\\f03e";
}
.uk-icon-pencil:before {
  content: "\\f040";
}
.uk-icon-map-marker:before {
  content: "\\f041";
}
.uk-icon-adjust:before {
  content: "\\f042";
}
.uk-icon-tint:before {
  content: "\\f043";
}
.uk-icon-edit:before,
.uk-icon-pencil-square-o:before {
  content: "\\f044";
}
.uk-icon-share-square-o:before {
  content: "\\f045";
}
.uk-icon-check-square-o:before {
  content: "\\f046";
}
.uk-icon-arrows:before {
  content: "\\f047";
}
.uk-icon-step-backward:before {
  content: "\\f048";
}
.uk-icon-fast-backward:before {
  content: "\\f049";
}
.uk-icon-backward:before {
  content: "\\f04a";
}
.uk-icon-play:before {
  content: "\\f04b";
}
.uk-icon-pause:before {
  content: "\\f04c";
}
.uk-icon-stop:before {
  content: "\\f04d";
}
.uk-icon-forward:before {
  content: "\\f04e";
}
.uk-icon-fast-forward:before {
  content: "\\f050";
}
.uk-icon-step-forward:before {
  content: "\\f051";
}
.uk-icon-eject:before {
  content: "\\f052";
}
.uk-icon-chevron-left:before {
  content: "\\f053";
}
.uk-icon-chevron-right:before {
  content: "\\f054";
}
.uk-icon-plus-circle:before {
  content: "\\f055";
}
.uk-icon-minus-circle:before {
  content: "\\f056";
}
.uk-icon-times-circle:before {
  content: "\\f057";
}
.uk-icon-check-circle:before {
  content: "\\f058";
}
.uk-icon-question-circle:before {
  content: "\\f059";
}
.uk-icon-info-circle:before {
  content: "\\f05a";
}
.uk-icon-crosshairs:before {
  content: "\\f05b";
}
.uk-icon-times-circle-o:before {
  content: "\\f05c";
}
.uk-icon-check-circle-o:before {
  content: "\\f05d";
}
.uk-icon-ban:before {
  content: "\\f05e";
}
.uk-icon-arrow-left:before {
  content: "\\f060";
}
.uk-icon-arrow-right:before {
  content: "\\f061";
}
.uk-icon-arrow-up:before {
  content: "\\f062";
}
.uk-icon-arrow-down:before {
  content: "\\f063";
}
.uk-icon-mail-forward:before,
.uk-icon-share:before {
  content: "\\f064";
}
.uk-icon-expand:before {
  content: "\\f065";
}
.uk-icon-compress:before {
  content: "\\f066";
}
.uk-icon-plus:before {
  content: "\\f067";
}
.uk-icon-minus:before {
  content: "\\f068";
}
.uk-icon-asterisk:before {
  content: "\\f069";
}
.uk-icon-exclamation-circle:before {
  content: "\\f06a";
}
.uk-icon-gift:before {
  content: "\\f06b";
}
.uk-icon-leaf:before {
  content: "\\f06c";
}
.uk-icon-fire:before {
  content: "\\f06d";
}
.uk-icon-eye:before {
  content: "\\f06e";
}
.uk-icon-eye-slash:before {
  content: "\\f070";
}
.uk-icon-warning:before,
.uk-icon-exclamation-triangle:before {
  content: "\\f071";
}
.uk-icon-plane:before {
  content: "\\f072";
}
.uk-icon-calendar:before {
  content: "\\f073";
}
.uk-icon-random:before {
  content: "\\f074";
}
.uk-icon-comment:before {
  content: "\\f075";
}
.uk-icon-magnet:before {
  content: "\\f076";
}
.uk-icon-chevron-up:before {
  content: "\\f077";
}
.uk-icon-chevron-down:before {
  content: "\\f078";
}
.uk-icon-retweet:before {
  content: "\\f079";
}
.uk-icon-shopping-cart:before {
  content: "\\f07a";
}
.uk-icon-folder:before {
  content: "\\f07b";
}
.uk-icon-folder-open:before {
  content: "\\f07c";
}
.uk-icon-arrows-v:before {
  content: "\\f07d";
}
.uk-icon-arrows-h:before {
  content: "\\f07e";
}
.uk-icon-bar-chart-o:before,
.uk-icon-bar-chart:before {
  content: "\\f080";
}
.uk-icon-twitter-square:before {
  content: "\\f081";
}
.uk-icon-facebook-square:before {
  content: "\\f082";
}
.uk-icon-camera-retro:before {
  content: "\\f083";
}
.uk-icon-key:before {
  content: "\\f084";
}
.uk-icon-gears:before,
.uk-icon-cogs:before {
  content: "\\f085";
}
.uk-icon-comments:before {
  content: "\\f086";
}
.uk-icon-thumbs-o-up:before {
  content: "\\f087";
}
.uk-icon-thumbs-o-down:before {
  content: "\\f088";
}
.uk-icon-star-half:before {
  content: "\\f089";
}
.uk-icon-heart-o:before {
  content: "\\f08a";
}
.uk-icon-sign-out:before {
  content: "\\f08b";
}
.uk-icon-linkedin-square:before {
  content: "\\f08c";
}
.uk-icon-thumb-tack:before {
  content: "\\f08d";
}
.uk-icon-external-link:before {
  content: "\\f08e";
}
.uk-icon-sign-in:before {
  content: "\\f090";
}
.uk-icon-trophy:before {
  content: "\\f091";
}
.uk-icon-github-square:before {
  content: "\\f092";
}
.uk-icon-upload:before {
  content: "\\f093";
}
.uk-icon-lemon-o:before {
  content: "\\f094";
}
.uk-icon-phone:before {
  content: "\\f095";
}
.uk-icon-square-o:before {
  content: "\\f096";
}
.uk-icon-bookmark-o:before {
  content: "\\f097";
}
.uk-icon-phone-square:before {
  content: "\\f098";
}
.uk-icon-twitter:before {
  content: "\\f099";
}
.uk-icon-facebook-f:before,
.uk-icon-facebook:before {
  content: "\\f09a";
}
.uk-icon-github:before {
  content: "\\f09b";
}
.uk-icon-unlock:before {
  content: "\\f09c";
}
.uk-icon-credit-card:before {
  content: "\\f09d";
}
.uk-icon-rss:before {
  content: "\\f09e";
}
.uk-icon-hdd-o:before {
  content: "\\f0a0";
}
.uk-icon-bullhorn:before {
  content: "\\f0a1";
}
.uk-icon-bell:before {
  content: "\\f0f3";
}
.uk-icon-certificate:before {
  content: "\\f0a3";
}
.uk-icon-hand-o-right:before {
  content: "\\f0a4";
}
.uk-icon-hand-o-left:before {
  content: "\\f0a5";
}
.uk-icon-hand-o-up:before {
  content: "\\f0a6";
}
.uk-icon-hand-o-down:before {
  content: "\\f0a7";
}
.uk-icon-arrow-circle-left:before {
  content: "\\f0a8";
}
.uk-icon-arrow-circle-right:before {
  content: "\\f0a9";
}
.uk-icon-arrow-circle-up:before {
  content: "\\f0aa";
}
.uk-icon-arrow-circle-down:before {
  content: "\\f0ab";
}
.uk-icon-globe:before {
  content: "\\f0ac";
}
.uk-icon-wrench:before {
  content: "\\f0ad";
}
.uk-icon-tasks:before {
  content: "\\f0ae";
}
.uk-icon-filter:before {
  content: "\\f0b0";
}
.uk-icon-briefcase:before {
  content: "\\f0b1";
}
.uk-icon-arrows-alt:before {
  content: "\\f0b2";
}
.uk-icon-group:before,
.uk-icon-users:before {
  content: "\\f0c0";
}
.uk-icon-chain:before,
.uk-icon-link:before {
  content: "\\f0c1";
}
.uk-icon-cloud:before {
  content: "\\f0c2";
}
.uk-icon-flask:before {
  content: "\\f0c3";
}
.uk-icon-cut:before,
.uk-icon-scissors:before {
  content: "\\f0c4";
}
.uk-icon-copy:before,
.uk-icon-files-o:before {
  content: "\\f0c5";
}
.uk-icon-paperclip:before {
  content: "\\f0c6";
}
.uk-icon-save:before,
.uk-icon-floppy-o:before {
  content: "\\f0c7";
}
.uk-icon-square:before {
  content: "\\f0c8";
}
.uk-icon-navicon:before,
.uk-icon-reorder:before,
.uk-icon-bars:before {
  content: "\\f0c9";
}
.uk-icon-list-ul:before {
  content: "\\f0ca";
}
.uk-icon-list-ol:before {
  content: "\\f0cb";
}
.uk-icon-strikethrough:before {
  content: "\\f0cc";
}
.uk-icon-underline:before {
  content: "\\f0cd";
}
.uk-icon-table:before {
  content: "\\f0ce";
}
.uk-icon-magic:before {
  content: "\\f0d0";
}
.uk-icon-truck:before {
  content: "\\f0d1";
}
.uk-icon-pinterest:before {
  content: "\\f0d2";
}
.uk-icon-pinterest-square:before {
  content: "\\f0d3";
}
.uk-icon-google-plus-square:before {
  content: "\\f0d4";
}
.uk-icon-google-plus:before {
  content: "\\f0d5";
}
.uk-icon-money:before {
  content: "\\f0d6";
}
.uk-icon-caret-down:before {
  content: "\\f0d7";
}
.uk-icon-caret-up:before {
  content: "\\f0d8";
}
.uk-icon-caret-left:before {
  content: "\\f0d9";
}
.uk-icon-caret-right:before {
  content: "\\f0da";
}
.uk-icon-columns:before {
  content: "\\f0db";
}
.uk-icon-unsorted:before,
.uk-icon-sort:before {
  content: "\\f0dc";
}
.uk-icon-sort-down:before,
.uk-icon-sort-desc:before {
  content: "\\f0dd";
}
.uk-icon-sort-up:before,
.uk-icon-sort-asc:before {
  content: "\\f0de";
}
.uk-icon-envelope:before {
  content: "\\f0e0";
}
.uk-icon-linkedin:before {
  content: "\\f0e1";
}
.uk-icon-rotate-left:before,
.uk-icon-undo:before {
  content: "\\f0e2";
}
.uk-icon-legal:before,
.uk-icon-gavel:before {
  content: "\\f0e3";
}
.uk-icon-dashboard:before,
.uk-icon-tachometer:before {
  content: "\\f0e4";
}
.uk-icon-comment-o:before {
  content: "\\f0e5";
}
.uk-icon-comments-o:before {
  content: "\\f0e6";
}
.uk-icon-flash:before,
.uk-icon-bolt:before {
  content: "\\f0e7";
}
.uk-icon-sitemap:before {
  content: "\\f0e8";
}
.uk-icon-umbrella:before {
  content: "\\f0e9";
}
.uk-icon-paste:before,
.uk-icon-clipboard:before {
  content: "\\f0ea";
}
.uk-icon-lightbulb-o:before {
  content: "\\f0eb";
}
.uk-icon-exchange:before {
  content: "\\f0ec";
}
.uk-icon-cloud-download:before {
  content: "\\f0ed";
}
.uk-icon-cloud-upload:before {
  content: "\\f0ee";
}
.uk-icon-user-md:before {
  content: "\\f0f0";
}
.uk-icon-stethoscope:before {
  content: "\\f0f1";
}
.uk-icon-suitcase:before {
  content: "\\f0f2";
}
.uk-icon-bell-o:before {
  content: "\\f0a2";
}
.uk-icon-coffee:before {
  content: "\\f0f4";
}
.uk-icon-cutlery:before {
  content: "\\f0f5";
}
.uk-icon-file-text-o:before {
  content: "\\f0f6";
}
.uk-icon-building-o:before {
  content: "\\f0f7";
}
.uk-icon-hospital-o:before {
  content: "\\f0f8";
}
.uk-icon-ambulance:before {
  content: "\\f0f9";
}
.uk-icon-medkit:before {
  content: "\\f0fa";
}
.uk-icon-fighter-jet:before {
  content: "\\f0fb";
}
.uk-icon-beer:before {
  content: "\\f0fc";
}
.uk-icon-h-square:before {
  content: "\\f0fd";
}
.uk-icon-plus-square:before {
  content: "\\f0fe";
}
.uk-icon-angle-double-left:before {
  content: "\\f100";
}
.uk-icon-angle-double-right:before {
  content: "\\f101";
}
.uk-icon-angle-double-up:before {
  content: "\\f102";
}
.uk-icon-angle-double-down:before {
  content: "\\f103";
}
.uk-icon-angle-left:before {
  content: "\\f104";
}
.uk-icon-angle-right:before {
  content: "\\f105";
}
.uk-icon-angle-up:before {
  content: "\\f106";
}
.uk-icon-angle-down:before {
  content: "\\f107";
}
.uk-icon-desktop:before {
  content: "\\f108";
}
.uk-icon-laptop:before {
  content: "\\f109";
}
.uk-icon-tablet:before {
  content: "\\f10a";
}
.uk-icon-mobile-phone:before,
.uk-icon-mobile:before {
  content: "\\f10b";
}
.uk-icon-circle-o:before {
  content: "\\f10c";
}
.uk-icon-quote-left:before {
  content: "\\f10d";
}
.uk-icon-quote-right:before {
  content: "\\f10e";
}
.uk-icon-spinner:before {
  content: "\\f110";
}
.uk-icon-circle:before {
  content: "\\f111";
}
.uk-icon-mail-reply:before,
.uk-icon-reply:before {
  content: "\\f112";
}
.uk-icon-github-alt:before {
  content: "\\f113";
}
.uk-icon-folder-o:before {
  content: "\\f114";
}
.uk-icon-folder-open-o:before {
  content: "\\f115";
}
.uk-icon-smile-o:before {
  content: "\\f118";
}
.uk-icon-frown-o:before {
  content: "\\f119";
}
.uk-icon-meh-o:before {
  content: "\\f11a";
}
.uk-icon-gamepad:before {
  content: "\\f11b";
}
.uk-icon-keyboard-o:before {
  content: "\\f11c";
}
.uk-icon-flag-o:before {
  content: "\\f11d";
}
.uk-icon-flag-checkered:before {
  content: "\\f11e";
}
.uk-icon-terminal:before {
  content: "\\f120";
}
.uk-icon-code:before {
  content: "\\f121";
}
.uk-icon-mail-reply-all:before,
.uk-icon-reply-all:before {
  content: "\\f122";
}
.uk-icon-star-half-empty:before,
.uk-icon-star-half-full:before,
.uk-icon-star-half-o:before {
  content: "\\f123";
}
.uk-icon-location-arrow:before {
  content: "\\f124";
}
.uk-icon-crop:before {
  content: "\\f125";
}
.uk-icon-code-fork:before {
  content: "\\f126";
}
.uk-icon-unlink:before,
.uk-icon-chain-broken:before {
  content: "\\f127";
}
.uk-icon-question:before {
  content: "\\f128";
}
.uk-icon-info:before {
  content: "\\f129";
}
.uk-icon-exclamation:before {
  content: "\\f12a";
}
.uk-icon-superscript:before {
  content: "\\f12b";
}
.uk-icon-subscript:before {
  content: "\\f12c";
}
.uk-icon-eraser:before {
  content: "\\f12d";
}
.uk-icon-puzzle-piece:before {
  content: "\\f12e";
}
.uk-icon-microphone:before {
  content: "\\f130";
}
.uk-icon-microphone-slash:before {
  content: "\\f131";
}
.uk-icon-shield:before {
  content: "\\f132";
}
.uk-icon-calendar-o:before {
  content: "\\f133";
}
.uk-icon-fire-extinguisher:before {
  content: "\\f134";
}
.uk-icon-rocket:before {
  content: "\\f135";
}
.uk-icon-maxcdn:before {
  content: "\\f136";
}
.uk-icon-chevron-circle-left:before {
  content: "\\f137";
}
.uk-icon-chevron-circle-right:before {
  content: "\\f138";
}
.uk-icon-chevron-circle-up:before {
  content: "\\f139";
}
.uk-icon-chevron-circle-down:before {
  content: "\\f13a";
}
.uk-icon-html5:before {
  content: "\\f13b";
}
.uk-icon-css3:before {
  content: "\\f13c";
}
.uk-icon-anchor:before {
  content: "\\f13d";
}
.uk-icon-unlock-alt:before {
  content: "\\f13e";
}
.uk-icon-bullseye:before {
  content: "\\f140";
}
.uk-icon-ellipsis-h:before {
  content: "\\f141";
}
.uk-icon-ellipsis-v:before {
  content: "\\f142";
}
.uk-icon-rss-square:before {
  content: "\\f143";
}
.uk-icon-play-circle:before {
  content: "\\f144";
}
.uk-icon-ticket:before {
  content: "\\f145";
}
.uk-icon-minus-square:before {
  content: "\\f146";
}
.uk-icon-minus-square-o:before {
  content: "\\f147";
}
.uk-icon-level-up:before {
  content: "\\f148";
}
.uk-icon-level-down:before {
  content: "\\f149";
}
.uk-icon-check-square:before {
  content: "\\f14a";
}
.uk-icon-pencil-square:before {
  content: "\\f14b";
}
.uk-icon-external-link-square:before {
  content: "\\f14c";
}
.uk-icon-share-square:before {
  content: "\\f14d";
}
.uk-icon-compass:before {
  content: "\\f14e";
}
.uk-icon-toggle-down:before,
.uk-icon-caret-square-o-down:before {
  content: "\\f150";
}
.uk-icon-toggle-up:before,
.uk-icon-caret-square-o-up:before {
  content: "\\f151";
}
.uk-icon-toggle-right:before,
.uk-icon-caret-square-o-right:before {
  content: "\\f152";
}
.uk-icon-euro:before,
.uk-icon-eur:before {
  content: "\\f153";
}
.uk-icon-gbp:before {
  content: "\\f154";
}
.uk-icon-dollar:before,
.uk-icon-usd:before {
  content: "\\f155";
}
.uk-icon-rupee:before,
.uk-icon-inr:before {
  content: "\\f156";
}
.uk-icon-cny:before,
.uk-icon-rmb:before,
.uk-icon-yen:before,
.uk-icon-jpy:before {
  content: "\\f157";
}
.uk-icon-ruble:before,
.uk-icon-rouble:before,
.uk-icon-rub:before {
  content: "\\f158";
}
.uk-icon-won:before,
.uk-icon-krw:before {
  content: "\\f159";
}
.uk-icon-bitcoin:before,
.uk-icon-btc:before {
  content: "\\f15a";
}
.uk-icon-file:before {
  content: "\\f15b";
}
.uk-icon-file-text:before {
  content: "\\f15c";
}
.uk-icon-sort-alpha-asc:before {
  content: "\\f15d";
}
.uk-icon-sort-alpha-desc:before {
  content: "\\f15e";
}
.uk-icon-sort-amount-asc:before {
  content: "\\f160";
}
.uk-icon-sort-amount-desc:before {
  content: "\\f161";
}
.uk-icon-sort-numeric-asc:before {
  content: "\\f162";
}
.uk-icon-sort-numeric-desc:before {
  content: "\\f163";
}
.uk-icon-thumbs-up:before {
  content: "\\f164";
}
.uk-icon-thumbs-down:before {
  content: "\\f165";
}
.uk-icon-youtube-square:before {
  content: "\\f166";
}
.uk-icon-youtube:before {
  content: "\\f167";
}
.uk-icon-xing:before {
  content: "\\f168";
}
.uk-icon-xing-square:before {
  content: "\\f169";
}
.uk-icon-youtube-play:before {
  content: "\\f16a";
}
.uk-icon-dropbox:before {
  content: "\\f16b";
}
.uk-icon-stack-overflow:before {
  content: "\\f16c";
}
.uk-icon-instagram:before {
  content: "\\f16d";
}
.uk-icon-flickr:before {
  content: "\\f16e";
}
.uk-icon-adn:before {
  content: "\\f170";
}
.uk-icon-bitbucket:before {
  content: "\\f171";
}
.uk-icon-bitbucket-square:before {
  content: "\\f172";
}
.uk-icon-tumblr:before {
  content: "\\f173";
}
.uk-icon-tumblr-square:before {
  content: "\\f174";
}
.uk-icon-long-arrow-down:before {
  content: "\\f175";
}
.uk-icon-long-arrow-up:before {
  content: "\\f176";
}
.uk-icon-long-arrow-left:before {
  content: "\\f177";
}
.uk-icon-long-arrow-right:before {
  content: "\\f178";
}
.uk-icon-apple:before {
  content: "\\f179";
}
.uk-icon-windows:before {
  content: "\\f17a";
}
.uk-icon-android:before {
  content: "\\f17b";
}
.uk-icon-linux:before {
  content: "\\f17c";
}
.uk-icon-dribbble:before {
  content: "\\f17d";
}
.uk-icon-skype:before {
  content: "\\f17e";
}
.uk-icon-foursquare:before {
  content: "\\f180";
}
.uk-icon-trello:before {
  content: "\\f181";
}
.uk-icon-female:before {
  content: "\\f182";
}
.uk-icon-male:before {
  content: "\\f183";
}
.uk-icon-gittip:before,
.uk-icon-gratipay:before {
  content: "\\f184";
}
.uk-icon-sun-o:before {
  content: "\\f185";
}
.uk-icon-moon-o:before {
  content: "\\f186";
}
.uk-icon-archive:before {
  content: "\\f187";
}
.uk-icon-bug:before {
  content: "\\f188";
}
.uk-icon-vk:before {
  content: "\\f189";
}
.uk-icon-weibo:before {
  content: "\\f18a";
}
.uk-icon-renren:before {
  content: "\\f18b";
}
.uk-icon-pagelines:before {
  content: "\\f18c";
}
.uk-icon-stack-exchange:before {
  content: "\\f18d";
}
.uk-icon-arrow-circle-o-right:before {
  content: "\\f18e";
}
.uk-icon-arrow-circle-o-left:before {
  content: "\\f190";
}
.uk-icon-toggle-left:before,
.uk-icon-caret-square-o-left:before {
  content: "\\f191";
}
.uk-icon-dot-circle-o:before {
  content: "\\f192";
}
.uk-icon-wheelchair:before {
  content: "\\f193";
}
.uk-icon-vimeo-square:before {
  content: "\\f194";
}
.uk-icon-turkish-lira:before,
.uk-icon-try:before {
  content: "\\f195";
}
.uk-icon-plus-square-o:before {
  content: "\\f196";
}
.uk-icon-space-shuttle:before {
  content: "\\f197";
}
.uk-icon-slack:before {
  content: "\\f198";
}
.uk-icon-envelope-square:before {
  content: "\\f199";
}
.uk-icon-wordpress:before {
  content: "\\f19a";
}
.uk-icon-openid:before {
  content: "\\f19b";
}
.uk-icon-institution:before,
.uk-icon-bank:before,
.uk-icon-university:before {
  content: "\\f19c";
}
.uk-icon-mortar-board:before,
.uk-icon-graduation-cap:before {
  content: "\\f19d";
}
.uk-icon-yahoo:before {
  content: "\\f19e";
}
.uk-icon-google:before {
  content: "\\f1a0";
}
.uk-icon-reddit:before {
  content: "\\f1a1";
}
.uk-icon-reddit-square:before {
  content: "\\f1a2";
}
.uk-icon-stumbleupon-circle:before {
  content: "\\f1a3";
}
.uk-icon-stumbleupon:before {
  content: "\\f1a4";
}
.uk-icon-delicious:before {
  content: "\\f1a5";
}
.uk-icon-digg:before {
  content: "\\f1a6";
}
.uk-icon-pied-piper:before {
  content: "\\f1a7";
}
.uk-icon-pied-piper-alt:before {
  content: "\\f1a8";
}
.uk-icon-drupal:before {
  content: "\\f1a9";
}
.uk-icon-joomla:before {
  content: "\\f1aa";
}
.uk-icon-language:before {
  content: "\\f1ab";
}
.uk-icon-fax:before {
  content: "\\f1ac";
}
.uk-icon-building:before {
  content: "\\f1ad";
}
.uk-icon-child:before {
  content: "\\f1ae";
}
.uk-icon-paw:before {
  content: "\\f1b0";
}
.uk-icon-spoon:before {
  content: "\\f1b1";
}
.uk-icon-cube:before {
  content: "\\f1b2";
}
.uk-icon-cubes:before {
  content: "\\f1b3";
}
.uk-icon-behance:before {
  content: "\\f1b4";
}
.uk-icon-behance-square:before {
  content: "\\f1b5";
}
.uk-icon-steam:before {
  content: "\\f1b6";
}
.uk-icon-steam-square:before {
  content: "\\f1b7";
}
.uk-icon-recycle:before {
  content: "\\f1b8";
}
.uk-icon-automobile:before,
.uk-icon-car:before {
  content: "\\f1b9";
}
.uk-icon-cab:before,
.uk-icon-taxi:before {
  content: "\\f1ba";
}
.uk-icon-tree:before {
  content: "\\f1bb";
}
.uk-icon-spotify:before {
  content: "\\f1bc";
}
.uk-icon-deviantart:before {
  content: "\\f1bd";
}
.uk-icon-soundcloud:before {
  content: "\\f1be";
}
.uk-icon-database:before {
  content: "\\f1c0";
}
.uk-icon-file-pdf-o:before {
  content: "\\f1c1";
}
.uk-icon-file-word-o:before {
  content: "\\f1c2";
}
.uk-icon-file-excel-o:before {
  content: "\\f1c3";
}
.uk-icon-file-powerpoint-o:before {
  content: "\\f1c4";
}
.uk-icon-file-photo-o:before,
.uk-icon-file-picture-o:before,
.uk-icon-file-image-o:before {
  content: "\\f1c5";
}
.uk-icon-file-zip-o:before,
.uk-icon-file-archive-o:before {
  content: "\\f1c6";
}
.uk-icon-file-sound-o:before,
.uk-icon-file-audio-o:before {
  content: "\\f1c7";
}
.uk-icon-file-movie-o:before,
.uk-icon-file-video-o:before {
  content: "\\f1c8";
}
.uk-icon-file-code-o:before {
  content: "\\f1c9";
}
.uk-icon-vine:before {
  content: "\\f1ca";
}
.uk-icon-codepen:before {
  content: "\\f1cb";
}
.uk-icon-jsfiddle:before {
  content: "\\f1cc";
}
.uk-icon-life-bouy:before,
.uk-icon-life-buoy:before,
.uk-icon-life-saver:before,
.uk-icon-support:before,
.uk-icon-life-ring:before {
  content: "\\f1cd";
}
.uk-icon-circle-o-notch:before {
  content: "\\f1ce";
}
.uk-icon-ra:before,
.uk-icon-rebel:before {
  content: "\\f1d0";
}
.uk-icon-ge:before,
.uk-icon-empire:before {
  content: "\\f1d1";
}
.uk-icon-git-square:before {
  content: "\\f1d2";
}
.uk-icon-git:before {
  content: "\\f1d3";
}
.uk-icon-hacker-news:before {
  content: "\\f1d4";
}
.uk-icon-tencent-weibo:before {
  content: "\\f1d5";
}
.uk-icon-qq:before {
  content: "\\f1d6";
}
.uk-icon-wechat:before,
.uk-icon-weixin:before {
  content: "\\f1d7";
}
.uk-icon-send:before,
.uk-icon-paper-plane:before {
  content: "\\f1d8";
}
.uk-icon-send-o:before,
.uk-icon-paper-plane-o:before {
  content: "\\f1d9";
}
.uk-icon-history:before {
  content: "\\f1da";
}
.uk-icon-genderless:before,
.uk-icon-circle-thin:before {
  content: "\\f1db";
}
.uk-icon-header:before {
  content: "\\f1dc";
}
.uk-icon-paragraph:before {
  content: "\\f1dd";
}
.uk-icon-sliders:before {
  content: "\\f1de";
}
.uk-icon-share-alt:before {
  content: "\\f1e0";
}
.uk-icon-share-alt-square:before {
  content: "\\f1e1";
}
.uk-icon-bomb:before {
  content: "\\f1e2";
}
.uk-icon-soccer-ball-o:before,
.uk-icon-futbol-o:before {
  content: "\\f1e3";
}
.uk-icon-tty:before {
  content: "\\f1e4";
}
.uk-icon-binoculars:before {
  content: "\\f1e5";
}
.uk-icon-plug:before {
  content: "\\f1e6";
}
.uk-icon-slideshare:before {
  content: "\\f1e7";
}
.uk-icon-twitch:before {
  content: "\\f1e8";
}
.uk-icon-yelp:before {
  content: "\\f1e9";
}
.uk-icon-newspaper-o:before {
  content: "\\f1ea";
}
.uk-icon-wifi:before {
  content: "\\f1eb";
}
.uk-icon-calculator:before {
  content: "\\f1ec";
}
.uk-icon-paypal:before {
  content: "\\f1ed";
}
.uk-icon-google-wallet:before {
  content: "\\f1ee";
}
.uk-icon-cc-visa:before {
  content: "\\f1f0";
}
.uk-icon-cc-mastercard:before {
  content: "\\f1f1";
}
.uk-icon-cc-discover:before {
  content: "\\f1f2";
}
.uk-icon-cc-amex:before {
  content: "\\f1f3";
}
.uk-icon-cc-paypal:before {
  content: "\\f1f4";
}
.uk-icon-cc-stripe:before {
  content: "\\f1f5";
}
.uk-icon-bell-slash:before {
  content: "\\f1f6";
}
.uk-icon-bell-slash-o:before {
  content: "\\f1f7";
}
.uk-icon-trash:before {
  content: "\\f1f8";
}
.uk-icon-copyright:before {
  content: "\\f1f9";
}
.uk-icon-at:before {
  content: "\\f1fa";
}
.uk-icon-eyedropper:before {
  content: "\\f1fb";
}
.uk-icon-paint-brush:before {
  content: "\\f1fc";
}
.uk-icon-birthday-cake:before {
  content: "\\f1fd";
}
.uk-icon-area-chart:before {
  content: "\\f1fe";
}
.uk-icon-pie-chart:before {
  content: "\\f200";
}
.uk-icon-line-chart:before {
  content: "\\f201";
}
.uk-icon-lastfm:before {
  content: "\\f202";
}
.uk-icon-lastfm-square:before {
  content: "\\f203";
}
.uk-icon-toggle-off:before {
  content: "\\f204";
}
.uk-icon-toggle-on:before {
  content: "\\f205";
}
.uk-icon-bicycle:before {
  content: "\\f206";
}
.uk-icon-bus:before {
  content: "\\f207";
}
.uk-icon-ioxhost:before {
  content: "\\f208";
}
.uk-icon-angellist:before {
  content: "\\f209";
}
.uk-icon-cc:before {
  content: "\\f20a";
}
.uk-icon-shekel:before,
.uk-icon-sheqel:before,
.uk-icon-ils:before {
  content: "\\f20b";
}
.uk-icon-meanpath:before {
  content: "\\f20c";
}
.uk-icon-buysellads:before {
  content: "\\f20d";
}
.uk-icon-connectdevelop:before {
  content: "\\f20e";
}
.uk-icon-dashcube:before {
  content: "\\f210";
}
.uk-icon-forumbee:before {
  content: "\\f211";
}
.uk-icon-leanpub:before {
  content: "\\f212";
}
.uk-icon-sellsy:before {
  content: "\\f213";
}
.uk-icon-shirtsinbulk:before {
  content: "\\f214";
}
.uk-icon-simplybuilt:before {
  content: "\\f215";
}
.uk-icon-skyatlas:before {
  content: "\\f216";
}
.uk-icon-cart-plus:before {
  content: "\\f217";
}
.uk-icon-cart-arrow-down:before {
  content: "\\f218";
}
.uk-icon-diamond:before {
  content: "\\f219";
}
.uk-icon-ship:before {
  content: "\\f21a";
}
.uk-icon-user-secret:before {
  content: "\\f21b";
}
.uk-icon-motorcycle:before {
  content: "\\f21c";
}
.uk-icon-street-view:before {
  content: "\\f21d";
}
.uk-icon-heartbeat:before {
  content: "\\f21e";
}
.uk-icon-venus:before {
  content: "\\f221";
}
.uk-icon-mars:before {
  content: "\\f222";
}
.uk-icon-mercury:before {
  content: "\\f223";
}
.uk-icon-transgender:before {
  content: "\\f224";
}
.uk-icon-transgender-alt:before {
  content: "\\f225";
}
.uk-icon-venus-double:before {
  content: "\\f226";
}
.uk-icon-mars-double:before {
  content: "\\f227";
}
.uk-icon-venus-mars:before {
  content: "\\f228";
}
.uk-icon-mars-stroke:before {
  content: "\\f229";
}
.uk-icon-mars-stroke-v:before {
  content: "\\f22a";
}
.uk-icon-mars-stroke-h:before {
  content: "\\f22b";
}
.uk-icon-neuter:before {
  content: "\\f22c";
}
.uk-icon-facebook-official:before {
  content: "\\f230";
}
.uk-icon-pinterest-p:before {
  content: "\\f231";
}
.uk-icon-whatsapp:before {
  content: "\\f232";
}
.uk-icon-server:before {
  content: "\\f233";
}
.uk-icon-user-plus:before {
  content: "\\f234";
}
.uk-icon-user-times:before {
  content: "\\f235";
}
.uk-icon-hotel:before,
.uk-icon-bed:before {
  content: "\\f236";
}
.uk-icon-viacoin:before {
  content: "\\f237";
}
.uk-icon-train:before {
  content: "\\f238";
}
.uk-icon-subway:before {
  content: "\\f239";
}
.uk-icon-medium-logo:before {
  content: "\\f23a";
}
.uk-icon-500px:before {
  content: "\\f26e";
}
.uk-icon-amazon:before {
  content: "\\f270";
}
.uk-icon-balance-scale:before {
  content: "\\f24e";
}
.uk-icon-battery-empty:before,
.uk-icon-battery-0:before {
  content: "\\f244";
}
.uk-icon-battery-quarter:before,
.uk-icon-battery-1:before {
  content: "\\f243";
}
.uk-icon-battery-half:before,
.uk-icon-battery-2:before {
  content: "\\f242";
}
.uk-icon-battery-three-quarters:before,
.uk-icon-battery-3:before {
  content: "\\f241";
}
.uk-icon-battery-full:before,
.uk-icon-battery-4:before {
  content: "\\f240";
}
.uk-icon-black-tie:before {
  content: "\\f27e";
}
.uk-icon-calendar-check-o:before {
  content: "\\f274";
}
.uk-icon-calendar-minus-o:before {
  content: "\\f272";
}
.uk-icon-calendar-plus-o:before {
  content: "\\f271";
}
.uk-icon-calendar-times-o:before {
  content: "\\f273";
}
.uk-icon-cc-diners-club:before {
  content: "\\f24c";
}
.uk-icon-cc-jcb:before {
  content: "\\f24b";
}
.uk-icon-chrome:before {
  content: "\\f268";
}
.uk-icon-clone:before {
  content: "\\f24d";
}
.uk-icon-commenting:before {
  content: "\\f27a";
}
.uk-icon-commenting-o:before {
  content: "\\f27b";
}
.uk-icon-contao:before {
  content: "\\f26d";
}
.uk-icon-creative-commons:before {
  content: "\\f25e";
}
.uk-icon-expeditedssl:before {
  content: "\\f23e";
}
.uk-icon-firefox:before {
  content: "\\f269";
}
.uk-icon-fonticons:before {
  content: "\\f280";
}
.uk-icon-get-pocket:before {
  content: "\\f265";
}
.uk-icon-gg:before {
  content: "\\f260";
}
.uk-icon-gg-circle:before {
  content: "\\f261";
}
.uk-icon-hand-lizard-o:before {
  content: "\\f258";
}
.uk-icon-hand-stop-o:before,
.uk-icon-hand-paper-o:before {
  content: "\\f256";
}
.uk-icon-hand-peace-o:before {
  content: "\\f25b";
}
.uk-icon-hand-pointer-o:before {
  content: "\\f25a";
}
.uk-icon-hand-grab-o:before,
.uk-icon-hand-rock-o:before {
  content: "\\f255";
}
.uk-icon-hand-scissors-o:before {
  content: "\\f257";
}
.uk-icon-hand-spock-o:before {
  content: "\\f259";
}
.uk-icon-hourglass:before {
  content: "\\f254";
}
.uk-icon-hourglass-o:before {
  content: "\\f250";
}
.uk-icon-hourglass-1:before,
.uk-icon-hourglass-start:before {
  content: "\\f251";
}
.uk-icon-hourglass-2:before,
.uk-icon-hourglass-half:before {
  content: "\\f252";
}
.uk-icon-hourglass-3:before,
.uk-icon-hourglass-end:before {
  content: "\\f253";
}
.uk-icon-houzz:before {
  content: "\\f27c";
}
.uk-icon-i-cursor:before {
  content: "\\f246";
}
.uk-icon-industry:before {
  content: "\\f275";
}
.uk-icon-internet-explorer:before {
  content: "\\f26b";
}
.uk-icon-map:before {
  content: "\\f279";
}
.uk-icon-map-o:before {
  content: "\\f278";
}
.uk-icon-map-pin:before {
  content: "\\f276";
}
.uk-icon-map-signs:before {
  content: "\\f277";
}
.uk-icon-mouse-pointer:before {
  content: "\\f245";
}
.uk-icon-object-group:before {
  content: "\\f247";
}
.uk-icon-object-ungroup:before {
  content: "\\f248";
}
.uk-icon-odnoklassniki:before {
  content: "\\f263";
}
.uk-icon-odnoklassniki-square:before {
  content: "\\f264";
}
.uk-icon-opencart:before {
  content: "\\f23d";
}
.uk-icon-opera:before {
  content: "\\f26a";
}
.uk-icon-optin-monster:before {
  content: "\\f23c";
}
.uk-icon-registered:before {
  content: "\\f25d";
}
.uk-icon-safari:before {
  content: "\\f267";
}
.uk-icon-sticky-note:before {
  content: "\\f249";
}
.uk-icon-sticky-note-o:before {
  content: "\\f24a";
}
.uk-icon-tv:before,
.uk-icon-television:before {
  content: "\\f26c";
}
.uk-icon-trademark:before {
  content: "\\f25c";
}
.uk-icon-tripadvisor:before {
  content: "\\f262";
}
.uk-icon-vimeo:before {
  content: "\\f27d";
}
.uk-icon-wikipedia-w:before {
  content: "\\f266";
}
.uk-icon-yc:before,
.uk-icon-y-combinator:before {
  content: "\\f23b";
}
.uk-icon-yc-square:before,
.uk-icon-y-combinator-square:before {
  content: "\\f1d4";
}
.uk-icon-bluetooth:before {
  content: "\\f293";
}
.uk-icon-bluetooth-b:before {
  content: "\\f294";
}
.uk-icon-codiepie:before {
  content: "\\f284";
}
.uk-icon-credit-card-alt:before {
  content: "\\f283";
}
.uk-icon-edge:before {
  content: "\\f282";
}
.uk-icon-fort-awesome:before {
  content: "\\f286";
}
.uk-icon-hashtag:before {
  content: "\\f292";
}
.uk-icon-mixcloud:before {
  content: "\\f289";
}
.uk-icon-modx:before {
  content: "\\f285";
}
.uk-icon-pause-circle:before {
  content: "\\f28b";
}
.uk-icon-pause-circle-o:before {
  content: "\\f28c";
}
.uk-icon-percent:before {
  content: "\\f295";
}
.uk-icon-product-hunt:before {
  content: "\\f288";
}
.uk-icon-reddit-alien:before {
  content: "\\f281";
}
.uk-icon-scribd:before {
  content: "\\f28a";
}
.uk-icon-shopping-bag:before {
  content: "\\f290";
}
.uk-icon-shopping-basket:before {
  content: "\\f291";
}
.uk-icon-stop-circle:before {
  content: "\\f28d";
}
.uk-icon-stop-circle-o:before {
  content: "\\f28e";
}
.uk-icon-usb:before {
  content: "\\f287";
}
.uk-icon-american-sign-language-interpreting:before,
.uk-icon-asl-interpreting:before {
  content: "\\f2a3";
}
.uk-icon-assistive-listening-systems:before {
  content: "\\f2a2";
}
.uk-icon-audio-description:before {
  content: "\\f29e";
}
.uk-icon-blind:before {
  content: "\\f29d";
}
.uk-icon-braille:before {
  content: "\\f2a1";
}
.uk-icon-deaf:before,
.uk-icon-deafness:before {
  content: "\\f2a4";
}
.uk-icon-envira:before {
  content: "\\f299";
}
.uk-icon-font-awesome:before,
.uk-icon-fa:before {
  content: "\\f2b4";
}
.uk-icon-first-order:before {
  content: "\\f2b0";
}
.uk-icon-gitlab:before {
  content: "\\f296";
}
.uk-icon-glide:before {
  content: "\\f2a5";
}
.uk-icon-glide-g:before {
  content: "\\f2a6";
}
.uk-icon-hard-of-hearing:before {
  content: "\\f2a4";
}
.uk-icon-low-vision:before {
  content: "\\f2a8";
}
.uk-icon-question-circle-o:before {
  content: "\\f29c";
}
.uk-icon-sign-language:before,
.uk-icon-signing:before {
  content: "\\f2a7";
}
.uk-icon-snapchat:before {
  content: "\\f2ab";
}
.uk-icon-snapchat-ghost:before {
  content: "\\f2ac";
}
.uk-icon-snapchat-square:before {
  content: "\\f2ad";
}
.uk-icon-themeisle:before {
  content: "\\f2b2";
}
.uk-icon-universal-access:before {
  content: "\\f29a";
}
.uk-icon-viadeo:before {
  content: "\\f2a9";
}
.uk-icon-viadeo-square:before {
  content: "\\f2aa";
}
.uk-icon-volume-control-phone:before {
  content: "\\f2a0";
}
.uk-icon-wheelchair-alt:before {
  content: "\\f29b";
}
.uk-icon-wpbeginner:before {
  content: "\\f297";
}
.uk-icon-wpforms:before {
  content: "\\f298";
}
.uk-icon-yoast:before {
  content: "\\f2b1";
}
/* ========================================================================
   Component: Close
 ========================================================================== */
/*
 * Removes inner padding and border in Firefox 4+.
 */
.uk-close::-moz-focus-inner {
  border: 0;
  padding: 0;
}
/*
 * 1. Correct inability to style clickable `input` types in iOS.
 * 2. Remove margins in Chrome, Safari and Opera.
 * 3. Remove borders for `button`.
 * 4. Address `overflow` set to `hidden` in IE 8/9/10/11.
 * 5. Correct `font` properties and `color` not being inherited for `button`.
 * 6. Address inconsistent `text-transform` inheritance which is only inherit in Firefox and IE
 * 7. Remove default `button` padding and background color
 * 8. Style
 */
.uk-close {
  /* 1 */
  -webkit-appearance: none;
  /* 2 */
  margin: 0;
  /* 3 */
  border: none;
  /* 4 */
  overflow: visible;
  /* 5 */
  font: inherit;
  color: inherit;
  /* 6 */
  text-transform: none;
  /* 7. */
  padding: 0;
  background: transparent;
  /* 8 */
  display: inline-block;
  box-sizing: content-box;
  width: 20px;
  line-height: 20px;
  text-align: center;
  vertical-align: middle;
  opacity: 0.3;
}
/* Icon */
.uk-close:after {
  display: block;
  content: "\\f00d";
  font-family: FontAwesome;
}
/*
 * Hover
 * 1. Apply hover style also to focus state
 * 2. Remove default focus style
 * 3. Required for `a` elements
 */
.uk-close:hover,
.uk-close:focus {
  opacity: 0.5;
  /* 2 */
  outline: none;
  /* 3 */
  color: inherit;
  text-decoration: none;
  cursor: pointer;
}
/* Modifier
 ========================================================================== */
.uk-close-alt {
  padding: 2px;
  border-radius: 50%;
  background: #fff;
  opacity: 1;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.1), 0 0 6px rgba(0, 0, 0, 0.3);
}
/* Hover */
.uk-close-alt:hover,
.uk-close-alt:focus {
  opacity: 1;
}
/* Icon */
.uk-close-alt:after {
  opacity: 0.5;
}
.uk-close-alt:hover:after,
.uk-close-alt:focus:after {
  opacity: 0.8;
}
/* ========================================================================
   Component: Badge
 ========================================================================== */
.uk-badge {
  display: inline-block;
  padding: 0 5px;
  background: #009dd8;
  font-size: 10px;
  font-weight: bold;
  line-height: 14px;
  color: #fff;
  text-align: center;
  vertical-align: middle;
  text-transform: none;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-bottom-color: rgba(0, 0, 0, 0.3);
  background-origin: border-box;
  background-image: -webkit-linear-gradient(top, #00b4f5, #008dc5);
  background-image: linear-gradient(to bottom, #00b4f5, #008dc5);
  border-radius: 2px;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
}
/*
 * Keep color when badge is a link
 */
a.uk-badge:hover {
  color: #fff;
}
/* Modifier: `uk-badge-notification`;
 ========================================================================== */
.uk-badge-notification {
  box-sizing: border-box;
  min-width: 18px;
  border-radius: 500px;
  font-size: 12px;
  line-height: 18px;
}
/* Color modifier
 ========================================================================== */
/*
 * Modifier: `uk-badge-success`
 */
.uk-badge-success {
  background-color: #82bb42;
  background-image: -webkit-linear-gradient(top, #9fd256, #6fac34);
  background-image: linear-gradient(to bottom, #9fd256, #6fac34);
}
/*
 * Modifier: `uk-badge-warning`
 */
.uk-badge-warning {
  background-color: #f9a124;
  background-image: -webkit-linear-gradient(top, #fbb450, #f89406);
  background-image: linear-gradient(to bottom, #fbb450, #f89406);
}
/*
 * Modifier: `uk-badge-danger`
 */
.uk-badge-danger {
  background-color: #d32c46;
  background-image: -webkit-linear-gradient(top, #ee465a, #c11a39);
  background-image: linear-gradient(to bottom, #ee465a, #c11a39);
}
/* ========================================================================
   Component: Alert
 ========================================================================== */
.uk-alert {
  margin-bottom: 15px;
  padding: 10px;
  background: #ebf7fd;
  color: #2d7091;
  border: 1px solid rgba(45, 112, 145, 0.3);
  border-radius: 4px;
  text-shadow: 0 1px 0 #fff;
}
/*
 * Add margin if adjacent element
 */
* + .uk-alert {
  margin-top: 15px;
}
/*
 * Remove margin from the last-child
 */
.uk-alert > :last-child {
  margin-bottom: 0;
}
/*
 * Keep color for headings if the default heading color is changed
 */
.uk-alert h1,
.uk-alert h2,
.uk-alert h3,
.uk-alert h4,
.uk-alert h5,
.uk-alert h6 {
  color: inherit;
}
/* Close in alert
 ========================================================================== */
.uk-alert > .uk-close:first-child {
  float: right;
}
/*
 * Remove margin from adjacent element
 */
.uk-alert > .uk-close:first-child + * {
  margin-top: 0;
}
/* Modifier: `uk-alert-success`
 ========================================================================== */
.uk-alert-success {
  background: #f2fae3;
  color: #659f13;
  border-color: rgba(101, 159, 19, 0.3);
}
/* Modifier: `uk-alert-warning`
 ========================================================================== */
.uk-alert-warning {
  background: #fffceb;
  color: #e28327;
  border-color: rgba(226, 131, 39, 0.3);
}
/* Modifier: `uk-alert-danger`
 ========================================================================== */
.uk-alert-danger {
  background: #fff1f0;
  color: #d85030;
  border-color: rgba(216, 80, 48, 0.3);
}
/* Modifier: `uk-alert-large`
 ========================================================================== */
.uk-alert-large {
  padding: 20px;
}
.uk-alert-large > .uk-close:first-child {
  margin: -10px -10px 0 0;
}
/* ========================================================================
   Component: Thumbnail
 ========================================================================== */
/*
 * 1. Container width fits its content
 * 2. Responsive behavior
 * 3. Corrects `max-width` behavior sed
 * 4. Required for `figure` element
 * 5. Style
 */
.uk-thumbnail {
  /* 1 */
  display: inline-block;
  /* 2 */
  max-width: 100%;
  /* 3 */
  box-sizing: border-box;
  /* 3 */
  margin: 0;
  /* 4 */
  padding: 4px;
  border: 1px solid #ddd;
  background: #fff;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
/*
 * Hover state for `a` elements
 * 1. Apply hover style also to focus state
 * 2. Needed for caption
 * 3. Remove default focus style
 */
a.uk-thumbnail:hover,
a.uk-thumbnail:focus {
  border-color: #aaaaaa;
  background-color: #fff;
  /* 2 */
  text-decoration: none;
  /* 3 */
  outline: none;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
}
/* Caption
 ========================================================================== */
.uk-thumbnail-caption {
  padding-top: 4px;
  text-align: center;
  color: #444;
}
/* Sizes
 ========================================================================== */
.uk-thumbnail-mini {
  width: 150px;
}
.uk-thumbnail-small {
  width: 200px;
}
.uk-thumbnail-medium {
  width: 300px;
}
.uk-thumbnail-large {
  width: 400px;
}
.uk-thumbnail-expand,
.uk-thumbnail-expand > img {
  width: 100%;
}
/* ========================================================================
   Component: Overlay
 ========================================================================== */
/*
 * 1. Container width fits its content
 * 2. Create position context
 * 3. Set max-width for responsive images to prevent `inline-block` consequences
 * 4. Remove the gap between the container and its child element
 * 5. Needed for transitions and to fixed wrong scaling calculation for images in Chrome
 * 6. Fixed `overflow: hidden` to be ignored with border-radius and CSS transforms in Webkit
 * 7. Reset margin
 */
.uk-overlay {
  /* 1 */
  display: inline-block;
  /* 2 */
  position: relative;
  /* 3 */
  max-width: 100%;
  /* 4 */
  vertical-align: middle;
  /* 5 */
  overflow: hidden;
  /* 6 */
  -webkit-transform: translateZ(0);
  /* 7 */
  margin: 0;
}
/* 6 for Safari */
.uk-overlay.uk-border-circle {
  -webkit-mask-image: -webkit-radial-gradient(circle, white 100%, black 100%);
}
/*
 * Remove margin from content
 */
.uk-overlay > :first-child {
  margin-bottom: 0;
}
/* Sub-object `uk-overlay-panel`
 ========================================================================== */
/*
 * 1. Position cover
 * 2. Style
 */
.uk-overlay-panel {
  /* 1 */
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  /* 2 */
  padding: 20px;
  color: #fff;
}
/*
 * Remove margin from the last-child
 */
.uk-overlay-panel > :last-child,
.uk-overlay-panel.uk-flex > * > :last-child {
  margin-bottom: 0;
}
/*
 * Keep color for headings if the default heading color is changed
 */
.uk-overlay-panel h1,
.uk-overlay-panel h2,
.uk-overlay-panel h3,
.uk-overlay-panel h4,
.uk-overlay-panel h5,
.uk-overlay-panel h6 {
  color: inherit;
}
.uk-overlay-panel a:not([class]) {
  color: inherit;
  text-decoration: underline;
}
.uk-overlay-panel a[class*='uk-icon-']:not(.uk-icon-button) {
  color: inherit;
}
/* Sub-object `uk-overlay-hover` and `uk-overlay-active`
 ========================================================================== */
.uk-overlay-hover:not(:hover):not(.uk-hover) .uk-overlay-panel:not(.uk-ignore) {
  opacity: 0;
}
.uk-overlay-active :not(.uk-active) > .uk-overlay-panel:not(.uk-ignore) {
  opacity: 0;
}
/* Modifier `uk-overlay-background`
 ========================================================================== */
.uk-overlay-background {
  background: rgba(0, 0, 0, 0.5);
}
/* Modifier `uk-overlay-image`
 ========================================================================== */
/*
 * Reset panel
 */
.uk-overlay-image {
  padding: 0;
}
/* Position modifiers
 ========================================================================== */
.uk-overlay-top {
  bottom: auto;
}
.uk-overlay-bottom {
  top: auto;
}
.uk-overlay-left {
  right: auto;
}
.uk-overlay-right {
  left: auto;
}
/* Sub-object `uk-overlay-icon`
 ========================================================================== */
.uk-overlay-icon:before {
  content: "\\f002";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 50px;
  height: 50px;
  margin-top: -25px;
  margin-left: -25px;
  font-size: 50px;
  line-height: 1;
  font-family: FontAwesome;
  text-align: center;
  color: #fff;
}
/* Transitions
 ========================================================================== */
.uk-overlay-fade,
.uk-overlay-scale,
.uk-overlay-spin,
.uk-overlay-grayscale,
.uk-overlay-blur,
[class*='uk-overlay-slide'] {
  transition-duration: 0.3s;
  transition-timing-function: ease-out;
  transition-property: opacity, transform, filter;
}
.uk-overlay-active .uk-overlay-fade,
.uk-overlay-active .uk-overlay-scale,
.uk-overlay-active .uk-overlay-spin,
.uk-overlay-active [class*='uk-overlay-slide'] {
  transition-duration: 0.8s;
}
/*
 * Fade
 */
.uk-overlay-fade {
  opacity: 0.7;
}
.uk-overlay-hover:hover .uk-overlay-fade,
.uk-overlay-hover.uk-hover .uk-overlay-fade,
.uk-overlay-active .uk-active > .uk-overlay-fade {
  opacity: 1;
}
/*
 * Scale
 */
.uk-overlay-scale {
  -webkit-transform: scale(1);
  transform: scale(1);
}
.uk-overlay-hover:hover .uk-overlay-scale,
.uk-overlay-hover.uk-hover .uk-overlay-scale,
.uk-overlay-active .uk-active > .uk-overlay-scale {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
/*
 * Spin
 */
.uk-overlay-spin {
  -webkit-transform: scale(1) rotate(0deg);
  transform: scale(1) rotate(0deg);
}
.uk-overlay-hover:hover .uk-overlay-spin,
.uk-overlay-hover.uk-hover .uk-overlay-spin,
.uk-overlay-active .uk-active > .uk-overlay-spin {
  -webkit-transform: scale(1.1) rotate(3deg);
  transform: scale(1.1) rotate(3deg);
}
/*
 * Grayscale
 */
.uk-overlay-grayscale {
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
}
.uk-overlay-hover:hover .uk-overlay-grayscale,
.uk-overlay-hover.uk-hover .uk-overlay-grayscale,
.uk-overlay-active .uk-active > .uk-overlay-grayscale {
  -webkit-filter: grayscale(0%);
  filter: grayscale(0%);
}
/*
 * Slide
 */
[class*='uk-overlay-slide'] {
  opacity: 0;
}
/* Top */
.uk-overlay-slide-top {
  -webkit-transform: translateY(-100%);
  transform: translateY(-100%);
}
/* Bottom */
.uk-overlay-slide-bottom {
  -webkit-transform: translateY(100%);
  transform: translateY(100%);
}
/* Left */
.uk-overlay-slide-left {
  -webkit-transform: translateX(-100%);
  transform: translateX(-100%);
}
/* Right */
.uk-overlay-slide-right {
  -webkit-transform: translateX(100%);
  transform: translateX(100%);
}
/* Hover */
.uk-overlay-hover:hover [class*='uk-overlay-slide'],
.uk-overlay-hover.uk-hover [class*='uk-overlay-slide'],
.uk-overlay-active .uk-active > [class*='uk-overlay-slide'] {
  opacity: 1;
  -webkit-transform: translateX(0) translateY(0);
  transform: translateX(0) translateY(0);
}
/* DEPRECATED
 * Sub-object `uk-overlay-area`
 ========================================================================== */
/*
 * 1. Set position
 * 2. Set style
 * 3. Fade-in transition
 */
.uk-overlay-area {
  /* 1 */
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  /* 2 */
  background: rgba(0, 0, 0, 0.3);
  /* 3 */
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
  -webkit-transform: translate3d(0, 0, 0);
}
/*
 * Hover
 * 1. `uk-hover` to support touch devices
 * 2. Use optional `uk-overlay-toggle` to trigger the overlay earlier
 */
.uk-overlay:hover .uk-overlay-area,
.uk-overlay.uk-hover .uk-overlay-area,
.uk-overlay-toggle:hover .uk-overlay-area,
.uk-overlay-toggle.uk-hover .uk-overlay-area {
  opacity: 1;
}
/*
 * Icon
 */
.uk-overlay-area:empty:before {
  content: "\\f002";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 50px;
  height: 50px;
  margin-top: -25px;
  margin-left: -25px;
  font-size: 50px;
  line-height: 1;
  font-family: FontAwesome;
  text-align: center;
  color: #fff;
}
/* DEPRECATED
 * Sub-object `uk-overlay-area-content`
 ========================================================================== */
/*
 * Remove whitespace between child elements when using `inline-block`
 * Needed for Firefox
 */
.uk-overlay-area:not(:empty) {
  font-size: 0.001px;
}
/*
 * 1. Needed for vertical alignment
 */
.uk-overlay-area:not(:empty):before {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}
/*
 * 1. Set vertical alignment
 * 2. Reset whitespace hack
 * 3. Set horizontal alignment
 * 4. Set style
 */
.uk-overlay-area-content {
  /* 1 */
  display: inline-block;
  box-sizing: border-box;
  width: 100%;
  vertical-align: middle;
  /* 2 */
  font-size: 1rem;
  /* 3 */
  text-align: center;
  /* 4 */
  padding: 0 15px;
  color: #fff;
}
/*
 * Remove margin from the last-child
 */
.uk-overlay-area-content > :last-child {
  margin-bottom: 0;
}
/*
 * Links in overlay area
 */
.uk-overlay-area-content a:not([class]),
.uk-overlay-area-content a:not([class]):hover {
  color: inherit;
}
/* DEPRECATED
 * Sub-object `uk-overlay-caption`
 ========================================================================== */
/*
 * 1. Set position
 * 2. Set style
 * 3. Fade-in transition
 */
.uk-overlay-caption {
  /* 1 */
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  /* 2 */
  padding: 15px;
  background: rgba(0, 0, 0, 0.5);
  color: #fff;
  /* 3 */
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
  -webkit-transform: translate3d(0, 0, 0);
}
/*
 * Hover
 * 1. `uk-hover` to support touch devices
 * 2. Use optional `uk-overlay-toggle` to trigger the overlay earlier
 */
.uk-overlay:hover .uk-overlay-caption,
.uk-overlay.uk-hover .uk-overlay-caption,
.uk-overlay-toggle:hover .uk-overlay-caption,
.uk-overlay-toggle.uk-hover .uk-overlay-caption {
  opacity: 1;
}
/* ========================================================================
   Component: Column
 ========================================================================== */
[class*='uk-column-'] {
  -webkit-column-gap: 25px;
  -moz-column-gap: 25px;
  column-gap: 25px;
}
/* Width modifiers
 ========================================================================== */
.uk-column-1-2 {
  -webkit-column-count: 2;
  -moz-column-count: 2;
  column-count: 2;
}
.uk-column-1-3 {
  -webkit-column-count: 3;
  -moz-column-count: 3;
  column-count: 3;
}
.uk-column-1-4 {
  -webkit-column-count: 4;
  -moz-column-count: 4;
  column-count: 4;
}
.uk-column-1-5 {
  -webkit-column-count: 5;
  -moz-column-count: 5;
  column-count: 5;
}
.uk-column-1-6 {
  -webkit-column-count: 6;
  -moz-column-count: 6;
  column-count: 6;
}
/* Phone landscape and bigger */
@media (min-width: 480px) {
  .uk-column-small-1-2 {
    -webkit-column-count: 2;
    -moz-column-count: 2;
    column-count: 2;
  }
  .uk-column-small-1-3 {
    -webkit-column-count: 3;
    -moz-column-count: 3;
    column-count: 3;
  }
  .uk-column-small-1-4 {
    -webkit-column-count: 4;
    -moz-column-count: 4;
    column-count: 4;
  }
  .uk-column-small-1-5 {
    -webkit-column-count: 5;
    -moz-column-count: 5;
    column-count: 5;
  }
  .uk-column-small-1-6 {
    -webkit-column-count: 6;
    -moz-column-count: 6;
    column-count: 6;
  }
}
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-column-medium-1-2 {
    -webkit-column-count: 2;
    -moz-column-count: 2;
    column-count: 2;
  }
  .uk-column-medium-1-3 {
    -webkit-column-count: 3;
    -moz-column-count: 3;
    column-count: 3;
  }
  .uk-column-medium-1-4 {
    -webkit-column-count: 4;
    -moz-column-count: 4;
    column-count: 4;
  }
  .uk-column-medium-1-5 {
    -webkit-column-count: 5;
    -moz-column-count: 5;
    column-count: 5;
  }
  .uk-column-medium-1-6 {
    -webkit-column-count: 6;
    -moz-column-count: 6;
    column-count: 6;
  }
}
/* Desktop and bigger */
@media (min-width: 960px) {
  .uk-column-large-1-2 {
    -webkit-column-count: 2;
    -moz-column-count: 2;
    column-count: 2;
  }
  .uk-column-large-1-3 {
    -webkit-column-count: 3;
    -moz-column-count: 3;
    column-count: 3;
  }
  .uk-column-large-1-4 {
    -webkit-column-count: 4;
    -moz-column-count: 4;
    column-count: 4;
  }
  .uk-column-large-1-5 {
    -webkit-column-count: 5;
    -moz-column-count: 5;
    column-count: 5;
  }
  .uk-column-large-1-6 {
    -webkit-column-count: 6;
    -moz-column-count: 6;
    column-count: 6;
  }
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  .uk-column-xlarge-1-2 {
    -webkit-column-count: 2;
    -moz-column-count: 2;
    column-count: 2;
  }
  .uk-column-xlarge-1-3 {
    -webkit-column-count: 3;
    -moz-column-count: 3;
    column-count: 3;
  }
  .uk-column-xlarge-1-4 {
    -webkit-column-count: 4;
    -moz-column-count: 4;
    column-count: 4;
  }
  .uk-column-xlarge-1-5 {
    -webkit-column-count: 5;
    -moz-column-count: 5;
    column-count: 5;
  }
  .uk-column-xlarge-1-6 {
    -webkit-column-count: 6;
    -moz-column-count: 6;
    column-count: 6;
  }
}
/* ========================================================================
   Component: Animation
 ========================================================================== */
[class*='uk-animation-'] {
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
  -webkit-animation-timing-function: ease-out;
  animation-timing-function: ease-out;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
/* Hide animated element if scrollspy is used */
@media screen {
  [data-uk-scrollspy*='uk-animation-']:not([data-uk-scrollspy*='target']) {
    opacity: 0;
  }
}
/*
 * Fade
 * Higher specificity (!important) needed because of reverse modifier
 */
.uk-animation-fade {
  -webkit-animation-name: uk-fade;
  animation-name: uk-fade;
  -webkit-animation-duration: 0.8s;
  animation-duration: 0.8s;
  -webkit-animation-timing-function: linear !important;
  animation-timing-function: linear !important;
}
/*
 * Fade with scale
 */
.uk-animation-scale-up {
  -webkit-animation-name: uk-fade-scale-02;
  animation-name: uk-fade-scale-02;
}
.uk-animation-scale-down {
  -webkit-animation-name: uk-fade-scale-18;
  animation-name: uk-fade-scale-18;
}
/*
 * Fade with slide
 */
.uk-animation-slide-top {
  -webkit-animation-name: uk-fade-top;
  animation-name: uk-fade-top;
}
.uk-animation-slide-bottom {
  -webkit-animation-name: uk-fade-bottom;
  animation-name: uk-fade-bottom;
}
.uk-animation-slide-left {
  -webkit-animation-name: uk-fade-left;
  animation-name: uk-fade-left;
}
.uk-animation-slide-right {
  -webkit-animation-name: uk-fade-right;
  animation-name: uk-fade-right;
}
/*
 * Scale
 */
.uk-animation-scale {
  -webkit-animation-name: uk-scale-12;
  animation-name: uk-scale-12;
}
/*
 * Shake
 */
.uk-animation-shake {
  -webkit-animation-name: uk-shake;
  animation-name: uk-shake;
}
/* Direction modifiers
 ========================================================================== */
.uk-animation-reverse {
  -webkit-animation-direction: reverse;
  animation-direction: reverse;
  -webkit-animation-timing-function: ease-in;
  animation-timing-function: ease-in;
}
/* Duration modifiers
========================================================================== */
.uk-animation-15 {
  -webkit-animation-duration: 15s;
  animation-duration: 15s;
}
/* Origin modifiers
========================================================================== */
.uk-animation-top-left {
  -webkit-transform-origin: 0 0;
  transform-origin: 0 0;
}
.uk-animation-top-center {
  -webkit-transform-origin: 50% 0;
  transform-origin: 50% 0;
}
.uk-animation-top-right {
  -webkit-transform-origin: 100% 0;
  transform-origin: 100% 0;
}
.uk-animation-middle-left {
  -webkit-transform-origin: 0 50%;
  transform-origin: 0 50%;
}
.uk-animation-middle-right {
  -webkit-transform-origin: 100% 50%;
  transform-origin: 100% 50%;
}
.uk-animation-bottom-left {
  -webkit-transform-origin: 0 100%;
  transform-origin: 0 100%;
}
.uk-animation-bottom-center {
  -webkit-transform-origin: 50% 100%;
  transform-origin: 50% 100%;
}
.uk-animation-bottom-right {
  -webkit-transform-origin: 100% 100%;
  transform-origin: 100% 100%;
}
/* Sub-object: `uk-animation-hover`
========================================================================== */
/*
 * Enable animation only on hover
 * Note: Firefox also needs this because animations are not triggered when switching between display `hidden` and `block`
 */
.uk-animation-hover:not(:hover),
.uk-animation-hover:not(:hover) [class*='uk-animation-'],
.uk-touch .uk-animation-hover:not(.uk-hover),
.uk-touch .uk-animation-hover:not(.uk-hover) [class*='uk-animation-'] {
  -webkit-animation-name: none;
  animation-name: none;
}
/* Keyframes: Fade
 * Used by dropdown, datepicker and slideshow component
 ========================================================================== */
@-webkit-keyframes uk-fade {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@keyframes uk-fade {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
/* Keyframes: Fade with slide
 ========================================================================== */
/*
 * Top
 */
@-webkit-keyframes uk-fade-top {
  0% {
    opacity: 0;
    -webkit-transform: translateY(-100%);
  }
  100% {
    opacity: 1;
    -webkit-transform: translateY(0);
  }
}
@keyframes uk-fade-top {
  0% {
    opacity: 0;
    transform: translateY(-100%);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
/*
 * Bottom
 */
@-webkit-keyframes uk-fade-bottom {
  0% {
    opacity: 0;
    -webkit-transform: translateY(100%);
  }
  100% {
    opacity: 1;
    -webkit-transform: translateY(0);
  }
}
@keyframes uk-fade-bottom {
  0% {
    opacity: 0;
    transform: translateY(100%);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
/*
 * Left
 */
@-webkit-keyframes uk-fade-left {
  0% {
    opacity: 0;
    -webkit-transform: translateX(-100%);
  }
  100% {
    opacity: 1;
    -webkit-transform: translateX(0);
  }
}
@keyframes uk-fade-left {
  0% {
    opacity: 0;
    transform: translateX(-100%);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}
/*
 * Right
 */
@-webkit-keyframes uk-fade-right {
  0% {
    opacity: 0;
    -webkit-transform: translateX(100%);
  }
  100% {
    opacity: 1;
    -webkit-transform: translateX(0);
  }
}
@keyframes uk-fade-right {
  0% {
    opacity: 0;
    transform: translateX(100%);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}
/* Keyframes: Fade with scale
 ========================================================================== */
/*
 * Scale by 0.2
 */
@-webkit-keyframes uk-fade-scale-02 {
  0% {
    opacity: 0;
    -webkit-transform: scale(0.2);
  }
  100% {
    opacity: 1;
    -webkit-transform: scale(1);
  }
}
@keyframes uk-fade-scale-02 {
  0% {
    opacity: 0;
    transform: scale(0.2);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
/*
 * Scale by 1.5
 * Used by slideshow component
 */
@-webkit-keyframes uk-fade-scale-15 {
  0% {
    opacity: 0;
    -webkit-transform: scale(1.5);
  }
  100% {
    opacity: 1;
    -webkit-transform: scale(1);
  }
}
@keyframes uk-fade-scale-15 {
  0% {
    opacity: 0;
    transform: scale(1.5);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
/*
 * Scale by 1.8
 */
@-webkit-keyframes uk-fade-scale-18 {
  0% {
    opacity: 0;
    -webkit-transform: scale(1.8);
  }
  100% {
    opacity: 1;
    -webkit-transform: scale(1);
  }
}
@keyframes uk-fade-scale-18 {
  0% {
    opacity: 0;
    transform: scale(1.8);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}
/* Keyframes: Slide
 * Used by slideshow component
 ========================================================================== */
/*
 * Left
 */
@-webkit-keyframes uk-slide-left {
  0% {
    -webkit-transform: translateX(-100%);
  }
  100% {
    -webkit-transform: translateX(0);
  }
}
@keyframes uk-slide-left {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}
/*
 * Right
 */
@-webkit-keyframes uk-slide-right {
  0% {
    -webkit-transform: translateX(100%);
  }
  100% {
    -webkit-transform: translateX(0);
  }
}
@keyframes uk-slide-right {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(0);
  }
}
/*
 * Left third
 */
@-webkit-keyframes uk-slide-left-33 {
  0% {
    -webkit-transform: translateX(33%);
  }
  100% {
    -webkit-transform: translateX(0);
  }
}
@keyframes uk-slide-left-33 {
  0% {
    transform: translateX(33%);
  }
  100% {
    transform: translateX(0);
  }
}
/*
 * Right third
 */
@-webkit-keyframes uk-slide-right-33 {
  0% {
    -webkit-transform: translateX(-33%);
  }
  100% {
    -webkit-transform: translateX(0);
  }
}
@keyframes uk-slide-right-33 {
  0% {
    transform: translateX(-33%);
  }
  100% {
    transform: translateX(0);
  }
}
/* Keyframes: Scale
 ========================================================================== */
@-webkit-keyframes uk-scale-12 {
  0% {
    -webkit-transform: scale(1.2);
  }
  100% {
    -webkit-transform: scale(1);
  }
}
@keyframes uk-scale-12 {
  0% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
/* Keyframes: Rotate
 * Used by icon component
 ========================================================================== */
@-webkit-keyframes uk-rotate {
  0% {
    -webkit-transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
  }
}
@keyframes uk-rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(359deg);
  }
}
/* Keyframes: Shake
 ========================================================================== */
@-webkit-keyframes uk-shake {
  0%,
  100% {
    -webkit-transform: translateX(0);
  }
  10% {
    -webkit-transform: translateX(-9px);
  }
  20% {
    -webkit-transform: translateX(8px);
  }
  30% {
    -webkit-transform: translateX(-7px);
  }
  40% {
    -webkit-transform: translateX(6px);
  }
  50% {
    -webkit-transform: translateX(-5px);
  }
  60% {
    -webkit-transform: translateX(4px);
  }
  70% {
    -webkit-transform: translateX(-3px);
  }
  80% {
    -webkit-transform: translateX(2px);
  }
  90% {
    -webkit-transform: translateX(-1px);
  }
}
@keyframes uk-shake {
  0%,
  100% {
    transform: translateX(0);
  }
  10% {
    transform: translateX(-9px);
  }
  20% {
    transform: translateX(8px);
  }
  30% {
    transform: translateX(-7px);
  }
  40% {
    transform: translateX(6px);
  }
  50% {
    transform: translateX(-5px);
  }
  60% {
    transform: translateX(4px);
  }
  70% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  90% {
    transform: translateX(-1px);
  }
}
/* Keyframes: Fade with slide fixed
 * Used by dropdown and search component
 ========================================================================== */
/*
 * Top fixed
 */
@-webkit-keyframes uk-slide-top-fixed {
  0% {
    opacity: 0;
    -webkit-transform: translateY(-10px);
  }
  100% {
    opacity: 1;
    -webkit-transform: translateY(0);
  }
}
@keyframes uk-slide-top-fixed {
  0% {
    opacity: 0;
    transform: translateY(-10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
/*
 * Bottom fixed
 */
@-webkit-keyframes uk-slide-bottom-fixed {
  0% {
    opacity: 0;
    -webkit-transform: translateY(10px);
  }
  100% {
    opacity: 1;
    -webkit-transform: translateY(0);
  }
}
@keyframes uk-slide-bottom-fixed {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
/* ========================================================================
   Component: Dropdown
 ========================================================================== */
/*
 * 1. Hide by default
 * 2. Set position
 * 3. Box-sizing is needed for `uk-dropdown-justify`
 * 4. Set width
 */
.uk-dropdown,
.uk-dropdown-blank {
  /* 1 */
  display: none;
  /* 2 */
  position: absolute;
  z-index: 1020;
  /* 3 */
  box-sizing: border-box;
  /* 4 */
  width: 200px;
}
/*
 * Dropdown style
 * 1. Reset button group whitespace hack
 */
.uk-dropdown {
  padding: 15px;
  background: #fff;
  color: #444;
  /* 1 */
  font-size: 1rem;
  vertical-align: top;
  border: 1px solid #cbcbcb;
  border-radius: 4px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
/*
 * 1. Show dropdown
 * 2. Set animation
 * 3. Needed for scale animation
 */
.uk-open > .uk-dropdown,
.uk-open > .uk-dropdown-blank {
  /* 1 */
  display: block;
  /* 2 */
  -webkit-animation: uk-fade 0.2s ease-in-out;
  animation: uk-fade 0.2s ease-in-out;
  /* 3 */
  -webkit-transform-origin: 0 0;
  transform-origin: 0 0;
}
/* Alignment modifiers
 ========================================================================== */
/*
 * Modifier
 */
.uk-dropdown-top {
  margin-top: -5px;
}
.uk-dropdown-bottom {
  margin-top: 5px;
}
.uk-dropdown-left {
  margin-left: -5px;
}
.uk-dropdown-right {
  margin-left: 5px;
}
/* Nav in dropdown
 ========================================================================== */
.uk-dropdown .uk-nav {
  margin: 0 -15px;
}
/* Grid and panel in dropdown
 ========================================================================== */
/*
* Vertical gutter
*/
/*
 * Grid
 * Higher specificity to override large gutter
 */
.uk-grid .uk-dropdown-grid + .uk-dropdown-grid {
  margin-top: 15px;
}
/* Panels */
.uk-dropdown-grid > [class*='uk-width-'] > .uk-panel + .uk-panel {
  margin-top: 15px;
}
/* Tablet and bigger */
@media (min-width: 768px) {
  /*
     * Horizontal gutter
     */
  .uk-dropdown:not(.uk-dropdown-stack) > .uk-dropdown-grid {
    margin-left: -15px;
    margin-right: -15px;
  }
  .uk-dropdown:not(.uk-dropdown-stack) > .uk-dropdown-grid > [class*='uk-width-'] {
    padding-left: 15px;
    padding-right: 15px;
  }
  /*
     * Column divider
     */
  .uk-dropdown:not(.uk-dropdown-stack) > .uk-dropdown-grid > [class*='uk-width-']:nth-child(n+2) {
    border-left: 1px solid #ddd;
  }
  /*
     * Width multiplier for dropdown columns
     */
  .uk-dropdown-width-2:not(.uk-dropdown-stack) {
    width: 400px;
  }
  .uk-dropdown-width-3:not(.uk-dropdown-stack) {
    width: 600px;
  }
  .uk-dropdown-width-4:not(.uk-dropdown-stack) {
    width: 800px;
  }
  .uk-dropdown-width-5:not(.uk-dropdown-stack) {
    width: 1000px;
  }
}
/* Phone landscape and smaller */
@media (max-width: 767px) {
  /*
     * Stack columns and take full width
     */
  .uk-dropdown-grid > [class*='uk-width-'] {
    width: 100%;
  }
  /*
     * Vertical gutter
     */
  .uk-dropdown-grid > [class*='uk-width-']:nth-child(n+2) {
    margin-top: 15px;
  }
}
/*
* Stack grid columns
*/
.uk-dropdown-stack > .uk-dropdown-grid > [class*='uk-width-'] {
  width: 100%;
}
.uk-dropdown-stack > .uk-dropdown-grid > [class*='uk-width-']:nth-child(n+2) {
  margin-top: 15px;
}
/* Modifier `uk-dropdown-small`
 ========================================================================== */
/*
 * Set min-width and text expands dropdown if needed
 */
.uk-dropdown-small {
  min-width: 150px;
  width: auto;
  padding: 5px;
  white-space: nowrap;
}
/*
 * Nav in dropdown
 */
.uk-dropdown-small .uk-nav {
  margin: 0 -5px;
}
/* Modifier: `uk-dropdown-navbar`
 ========================================================================== */
.uk-dropdown-navbar {
  margin-top: 6px;
  background: #fff;
  color: #444;
  left: -1px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
.uk-open > .uk-dropdown-navbar {
  -webkit-animation: uk-slide-top-fixed 0.2s ease-in-out;
  animation: uk-slide-top-fixed 0.2s ease-in-out;
}
/* Modifier `uk-dropdown-scrollable`
 ========================================================================== */
/*
 * Usefull for long lists
 */
.uk-dropdown-scrollable {
  overflow-y: auto;
  max-height: 200px;
}
/* Sub-object: `uk-dropdown-overlay`
 ========================================================================== */
.uk-dropdown-navbar.uk-dropdown-flip {
  left: auto;
}
/* ========================================================================
   Component: Modal
 ========================================================================== */
/*
 * This is the modal overlay and modal dialog container
 * 1. Hide by default
 * 2. Set fixed position
 * 3. Allow scrolling for the modal dialog
 * 4. Mask the background page
 * 5. Fade-in transition
 * 6. Deactivate browser history navigation in IE11
 * 7. force hardware acceleration to prevent browser rendering hiccups
 */
.uk-modal {
  /* 1 */
  display: none;
  /* 2 */
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1010;
  /* 3 */
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  /* 4 */
  background: rgba(0, 0, 0, 0.6);
  /* 5 */
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
  /* 6 */
  touch-action: cross-slide-y pinch-zoom double-tap-zoom;
  /* 7 */
  -webkit-transform: translateZ(0);
  transform: translateZ(0);
}
/*
 * Open state
 */
.uk-modal.uk-open {
  opacity: 1;
}
/*
 * Prevents duplicated scrollbar caused by 4.
 */
.uk-modal-page,
.uk-modal-page body {
  overflow: hidden;
}
/* Sub-object: `uk-modal-dialog`
 ========================================================================== */
/*
 * 1. Create position context for caption, spinner and close button
 * 2. Set box sizing
 * 3. Set style
 * 4. Slide-in transition
 */
.uk-modal-dialog {
  /* 1 */
  position: relative;
  /* 2 */
  box-sizing: border-box;
  margin: 50px auto;
  padding: 20px;
  width: 600px;
  max-width: 100%;
  max-width: calc(100% - 20px);
  /* 3 */
  background: #fff;
  /* 4 */
  opacity: 0;
  -webkit-transform: translateY(-100px);
  transform: translateY(-100px);
  -webkit-transition: opacity 0.3s linear, -webkit-transform 0.3s ease-out;
  transition: opacity 0.3s linear, transform 0.3s ease-out;
  border-radius: 4px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}
/* Phone landscape and smaller */
@media (max-width: 767px) {
  /*
     * Fit in small screen
     */
  .uk-modal-dialog {
    width: auto;
    margin: 10px auto;
  }
}
/*
 * Open state
 */
.uk-open .uk-modal-dialog {
  /* 4 */
  opacity: 1;
  -webkit-transform: translateY(0);
  transform: translateY(0);
}
/*
 * Remove margin from the last-child
 */
.uk-modal-dialog > :not([class*='uk-modal-']):last-child {
  margin-bottom: 0;
}
/* Close in modal
 ========================================================================== */
.uk-modal-dialog > .uk-close:first-child {
  margin: -10px -10px 0 0;
  float: right;
}
/*
 * Remove margin from adjacent element
 */
.uk-modal-dialog > .uk-close:first-child + :not([class*='uk-modal-']) {
  margin-top: 0;
}
/* Modifier: `uk-modal-dialog-lightbox`
 ========================================================================== */
.uk-modal-dialog-lightbox {
  margin: 15px auto;
  padding: 0;
  max-width: 95%;
  max-width: calc(100% - 30px);
  min-height: 50px;
  border-radius: 0;
}
/*
 * Close button
 */
.uk-modal-dialog-lightbox > .uk-close:first-child {
  position: absolute;
  top: -12px;
  right: -12px;
  margin: 0;
  float: none;
}
/* Phone landscape and smaller */
@media (max-width: 767px) {
  .uk-modal-dialog-lightbox > .uk-close:first-child {
    top: -7px;
    right: -7px;
  }
}
/* Modifier: `uk-modal-dialog-blank`
 ========================================================================== */
.uk-modal-dialog-blank {
  margin: 0;
  padding: 0;
  width: 100%;
  max-width: 100%;
  -webkit-transition: opacity 0.3s linear;
  transition: opacity 0.3s linear;
}
/*
* Close button
*/
.uk-modal-dialog-blank > .uk-close:first-child {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 1;
  margin: 0;
  float: none;
}
/* Modifier: `uk-modal-dialog-large`
 ========================================================================== */
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-modal-dialog-large {
    width: 930px;
  }
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  .uk-modal-dialog-large {
    width: 1130px;
  }
}
/* Sub-Object: `uk-modal-header` and `uk-modal-footer`
 ========================================================================== */
.uk-modal-header {
  margin-bottom: 15px;
  margin: -20px -20px 15px -20px;
  padding: 20px;
  border-bottom: 1px solid #ddd;
  border-radius: 4px 4px 0 0;
  background: #fafafa;
}
.uk-modal-footer {
  margin-top: 15px;
  margin: 15px -20px -20px -20px;
  padding: 20px;
  border-top: 1px solid #ddd;
  border-radius: 0 0 4px 4px;
  background: #fafafa;
}
/*
 * Remove margin from the last-child
 */
.uk-modal-header > :last-child,
.uk-modal-footer > :last-child {
  margin-bottom: 0;
}
/* Sub-Object: `uk-modal-caption`
 ========================================================================== */
.uk-modal-caption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -20px;
  margin-bottom: -10px;
  color: #fff;
  text-align: center;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
/* Sub-Object: `uk-modal-spinner`
 ========================================================================== */
.uk-modal-spinner {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  font-size: 25px;
  color: #ddd;
}
.uk-modal-spinner:after {
  content: "\\f110";
  display: block;
  font-family: FontAwesome;
  -webkit-animation: uk-rotate 2s infinite linear;
  animation: uk-rotate 2s infinite linear;
}
/* ========================================================================
   Component: Off-canvas
 ========================================================================== */
/*
 * This is the offcanvas overlay and bar container
 * 1. Hide by default
 * 2. Set fixed position
 * 3. Deactivate browser touch actions in IE11
 * 4. Mask the background page
 */
.uk-offcanvas {
  /* 1 */
  display: none;
  /* 2 */
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1000;
  /* 3 */
  touch-action: none;
  /* 4 */
  background: rgba(0, 0, 0, 0.1);
}
.uk-offcanvas.uk-active {
  display: block;
}
/* Sub-object `uk-offcanvas-page`
 ========================================================================== */
/*
 * Prepares the whole HTML page to slide-out
 * 1. Fix the main page and disallow scrolling
 * 2. Side-out transition
 * 3. Needed for the transition to work instead of just letting it pop to the side
 */
.uk-offcanvas-page {
  /* 1 */
  position: fixed;
  /* 2 */
  -webkit-transition: margin-left 0.3s ease-in-out;
  transition: margin-left 0.3s ease-in-out;
  /* 3 */
  margin-left: 0;
}
/* Sub-object `uk-offcanvas-bar`
 ========================================================================== */
/*
 * This is the offcanvas bar
 * 1. Set fixed position
 * 2. Size and style
 * 3. Allow scrolling
 * 4. Side-out transition
 * 5. Deactivate scroll chaining in IE11
 */
.uk-offcanvas-bar {
  /* 1 */
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  -webkit-transform: translateX(-100%);
  transform: translateX(-100%);
  z-index: 1001;
  /* 2 */
  width: 270px;
  max-width: 100%;
  background: #333;
  /* 3 */
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  /* 4 */
  -webkit-transition: -webkit-transform 0.3s ease-in-out;
  transition: transform 0.3s ease-in-out;
  /* 5 */
  -ms-scroll-chaining: none;
}
.uk-offcanvas.uk-active .uk-offcanvas-bar.uk-offcanvas-bar-show {
  -webkit-transform: translateX(0%);
  transform: translateX(0%);
}
/* Modifier `uk-offcanvas-bar-flip`
 ========================================================================== */
.uk-offcanvas-bar-flip {
  left: auto;
  right: 0;
  -webkit-transform: translateX(100%);
  transform: translateX(100%);
}
/* Offcanvase modes
 ========================================================================== */
.uk-offcanvas-bar[mode='none'] {
  -webkit-transition: none;
  transition: none;
}
.uk-offcanvas-bar[mode='reveal'] {
  -webkit-transform: translateX(0%);
  transform: translateX(0%);
  clip: rect(0, 0, 100vh, 0);
  -webkit-transition: -webkit-transform 0.3s ease-in-out, clip 0.3s ease-in-out;
  transition: transform 0.3s ease-in-out, clip 0.3s ease-in-out;
}
.uk-offcanvas-bar-flip[mode='reveal'] {
  clip: none;
  -webkit-transform: translateX(100%);
  transform: translateX(100%);
}
.uk-offcanvas-bar-flip[mode='reveal'] > * {
  -webkit-transform: translateX(-100%);
  transform: translateX(-100%);
  -webkit-transition: -webkit-transform 0.3s ease-in-out;
  transition: transform 0.3s ease-in-out;
}
.uk-offcanvas.uk-active .uk-offcanvas-bar-flip[mode='reveal'].uk-offcanvas-bar-show > * {
  -webkit-transform: translateX(0%);
  transform: translateX(0%);
}
/* Panel in offcanvas
 ========================================================================== */
.uk-offcanvas .uk-panel {
  margin: 20px 15px;
  color: #777;
  text-shadow: 0 1px 0 rgba(0, 0, 0, 0.5);
}
.uk-offcanvas .uk-panel-title {
  color: #ccc;
}
.uk-offcanvas .uk-panel a:not([class]) {
  color: #ccc;
}
.uk-offcanvas .uk-panel a:not([class]):hover {
  color: #fff;
}
.uk-offcanvas-bar:after {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 1px;
  background: rgba(0, 0, 0, 0.6);
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.6);
}
.uk-offcanvas-bar-flip:after {
  right: auto;
  left: 0;
  width: 1px;
  background: rgba(0, 0, 0, 0.6);
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.6);
}
/* ========================================================================
   Component: Switcher
 ========================================================================== */
/*
 * 1. Deactivate browser history navigation in IE11
 */
.uk-switcher {
  margin: 0;
  padding: 0;
  list-style: none;
  /* 1 */
  touch-action: cross-slide-y pinch-zoom double-tap-zoom;
}
/*
 * Items
 */
.uk-switcher > :not(.uk-active) {
  display: none;
}
/* ========================================================================
   Component: Text
 ========================================================================== */
/* Size modifiers
 ========================================================================== */
.uk-text-small {
  font-size: 11px;
  line-height: 16px;
}
.uk-text-large {
  font-size: 18px;
  line-height: 24px;
  font-weight: normal;
}
/* Weight modifiers
 ========================================================================== */
.uk-text-bold {
  font-weight: bold;
}
/* Color modifiers
 ========================================================================== */
.uk-text-muted {
  color: #999 !important;
}
.uk-text-primary {
  color: #2d7091 !important;
}
.uk-text-success {
  color: #659f13 !important;
}
.uk-text-warning {
  color: #e28327 !important;
}
.uk-text-danger {
  color: #d85030 !important;
}
.uk-text-contrast {
  color: #fff !important;
}
/* Alignment modifiers
 ========================================================================== */
.uk-text-left {
  text-align: left !important;
}
.uk-text-right {
  text-align: right !important;
}
.uk-text-center {
  text-align: center !important;
}
.uk-text-justify {
  text-align: justify !important;
}
.uk-text-top {
  vertical-align: top !important;
}
.uk-text-middle {
  vertical-align: middle !important;
}
.uk-text-bottom {
  vertical-align: bottom !important;
}
/* Only tablets portrait and smaller */
@media (max-width: 959px) {
  .uk-text-center-medium {
    text-align: center !important;
  }
  .uk-text-left-medium {
    text-align: left !important;
  }
}
/* Phone landscape and smaller */
@media (max-width: 767px) {
  .uk-text-center-small {
    text-align: center !important;
  }
  .uk-text-left-small {
    text-align: left !important;
  }
}
/* Wrap modifiers
 ========================================================================== */
/*
 * Prevent text from wrapping onto multiple lines
 */
.uk-text-nowrap {
  white-space: nowrap;
}
/*
 * Prevent text from wrapping onto multiple lines, and truncate with an ellipsis
 */
.uk-text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
/*
 * Break strings if their length exceeds the width of their container
 */
.uk-text-break {
  word-wrap: break-word;
  -webkit-hyphens: auto;
  -ms-hyphens: auto;
  -moz-hyphens: auto;
  hyphens: auto;
}
/* Transform modifiers
 ========================================================================== */
.uk-text-capitalize {
  text-transform: capitalize !important;
}
.uk-text-lowercase {
  text-transform: lowercase !important;
}
.uk-text-uppercase {
  text-transform: uppercase !important;
}
/* ========================================================================
   Component: Utility
 ========================================================================== */
/* Container
 ========================================================================== */
.uk-container {
  box-sizing: border-box;
  max-width: 980px;
  padding: 0 25px;
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  .uk-container {
    max-width: 1200px;
    padding: 0 35px;
  }
}
/*
 * Micro clearfix
 */
.uk-container:before,
.uk-container:after {
  content: "";
  display: table;
}
.uk-container:after {
  clear: both;
}
/*
 * Center container
 */
.uk-container-center {
  margin-left: auto;
  margin-right: auto;
}
/* Clearing
 ========================================================================== */
/*
 * Micro clearfix
* `table-cell` is used with `:before` because `table` creates a 1px gap when it becomes a flex item, only in Webkit
 * `table` is used again with `:after` because `clear` only works with block elements.
 * Note: `display: block` with `overflow: hidden` is currently not working in the latest Safari
 */
.uk-clearfix:before {
  content: "";
  display: table-cell;
}
.uk-clearfix:after {
  content: "";
  display: table;
  clear: both;
}
/*
 *  Create a new block formatting context
 */
.uk-nbfc {
  overflow: hidden;
}
.uk-nbfc-alt {
  display: table-cell;
  width: 10000px;
}
/* Alignment of block elements
 ========================================================================== */
/*
 * Float blocks
 * 1. Prevent content overflow on small devices
 */
.uk-float-left {
  float: left;
}
.uk-float-right {
  float: right;
}
/* 1 */
[class*='uk-float-'] {
  max-width: 100%;
}
/* Alignment of images and objects
 ========================================================================== */
/*
 * Alignment
 */
[class*='uk-align-'] {
  display: block;
  margin-bottom: 15px;
}
.uk-align-left {
  margin-right: 15px;
  float: left;
}
.uk-align-right {
  margin-left: 15px;
  float: right;
}
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-align-medium-left {
    margin-right: 15px;
    float: left;
  }
  .uk-align-medium-right {
    margin-left: 15px;
    float: right;
  }
}
.uk-align-center {
  margin-left: auto;
  margin-right: auto;
}
/* Vertical alignment
 ========================================================================== */
/*
 * Remove whitespace between child elements when using `inline-block`
 */
.uk-vertical-align {
  font-size: 0.001px;
}
/*
 *  The `uk-vertical-align` container needs a specific height
 */
.uk-vertical-align:before {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}
/*
 * Sub-object which can have any height
 * 1. Reset whitespace hack
 */
.uk-vertical-align-middle,
.uk-vertical-align-bottom {
  display: inline-block;
  max-width: 100%;
  /* 1 */
  font-size: 1rem;
}
.uk-vertical-align-middle {
  vertical-align: middle;
}
.uk-vertical-align-bottom {
  vertical-align: bottom;
}
/* Height
 ========================================================================== */
/*
 * More robust if padding and border are used
 */
[class*='uk-height'] {
  box-sizing: border-box;
}
/*
 * Useful to extend the `html` and `body` element to the full height of the page.
 */
.uk-height-1-1 {
  height: 100%;
}
/*
 * Useful to create image teasers
 */
.uk-height-viewport {
  height: 100vh;
  min-height: 600px;
}
/* Responsive objects
 * Note: Images are already responsive by default, see Base component
 ========================================================================== */
/*
 * 1. Corrects `max-width` and `max-height` behavior if padding and border are used
 */
.uk-responsive-width,
.uk-responsive-height {
  box-sizing: border-box;
}
/*
 * Responsiveness: Sets a maximum width relative to the parent and auto scales the height
 * `important` needed to override `uk-img-preserve img`
 */
.uk-responsive-width {
  max-width: 100% !important;
  height: auto;
}
/*
 * Responsiveness: Sets a maximum height relative to the parent and auto scales the width
 * Only works if the parent element has a fixed height.
 */
.uk-responsive-height {
  max-height: 100%;
  width: auto;
}
/* Margin
 ========================================================================== */
/*
 * Create a block with the same margin of a paragraph
 * Add margin if adjacent element
 */
.uk-margin {
  margin-bottom: 15px;
}
* + .uk-margin {
  margin-top: 15px;
}
.uk-margin-top {
  margin-top: 15px !important;
}
.uk-margin-bottom {
  margin-bottom: 15px !important;
}
.uk-margin-left {
  margin-left: 15px !important;
}
.uk-margin-right {
  margin-right: 15px !important;
}
/*
 * Larger margins
 */
.uk-margin-large {
  margin-bottom: 50px;
}
* + .uk-margin-large {
  margin-top: 50px;
}
.uk-margin-large-top {
  margin-top: 50px !important;
}
.uk-margin-large-bottom {
  margin-bottom: 50px !important;
}
.uk-margin-large-left {
  margin-left: 50px !important;
}
.uk-margin-large-right {
  margin-right: 50px !important;
}
/*
 * Smaller margins
 */
.uk-margin-small {
  margin-bottom: 5px;
}
* + .uk-margin-small {
  margin-top: 5px;
}
.uk-margin-small-top {
  margin-top: 5px !important;
}
.uk-margin-small-bottom {
  margin-bottom: 5px !important;
}
.uk-margin-small-left {
  margin-left: 5px !important;
}
.uk-margin-small-right {
  margin-right: 5px !important;
}
/*
 * Remove margins
 */
.uk-margin-remove {
  margin: 0 !important;
}
.uk-margin-top-remove {
  margin-top: 0 !important;
}
.uk-margin-bottom-remove {
  margin-bottom: 0 !important;
}
/* Padding
 ========================================================================== */
.uk-padding-remove {
  padding: 0 !important;
}
.uk-padding-top-remove {
  padding-top: 0 !important;
}
.uk-padding-bottom-remove {
  padding-bottom: 0 !important;
}
.uk-padding-vertical-remove {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}
/* Border
 ========================================================================== */
.uk-border-circle {
  border-radius: 50%;
}
.uk-border-rounded {
  border-radius: 5px;
}
/* Headings
 ========================================================================== */
.uk-heading-large {
  font-size: 36px;
  line-height: 42px;
}
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-heading-large {
    font-size: 52px;
    line-height: 64px;
  }
}
/* Link
 ========================================================================== */
/*
 * Let links appear in default text color
 */
.uk-link-muted,
.uk-link-muted a {
  color: #444;
}
.uk-link-muted:hover,
.uk-link-muted a:hover {
  color: #444;
}
/*
 * Reset link style
 */
.uk-link-reset,
.uk-link-reset a,
.uk-link-reset:hover,
.uk-link-reset a:hover,
.uk-link-reset:focus,
.uk-link-reset a:focus {
  color: inherit;
  text-decoration: none;
}
/* Scrollable
 ========================================================================== */
/*
 * Enable scrolling for preformatted text
 */
.uk-scrollable-text {
  height: 300px;
  overflow-y: scroll;
  -webkit-overflow-scrolling: touch;
  resize: both;
}
/*
 * Box with scrolling enabled
 */
.uk-scrollable-box {
  box-sizing: border-box;
  height: 170px;
  padding: 10px;
  border: 1px solid #ddd;
  overflow: auto;
  -webkit-overflow-scrolling: touch;
  resize: both;
  border-radius: 3px;
}
.uk-scrollable-box > :last-child {
  margin-bottom: 0;
}
/* Overflow
 ========================================================================== */
.uk-overflow-hidden {
  overflow: hidden;
}
/*
 * Enable scrollbars if content is clipped
 */
.uk-overflow-container {
  overflow: auto;
  -webkit-overflow-scrolling: touch;
}
.uk-overflow-container > :last-child {
  margin-bottom: 0;
}
/* Position
 ========================================================================== */
.uk-position-absolute,
[class*='uk-position-top'],
[class*='uk-position-bottom'] {
  position: absolute !important;
}
/* Don't use `width: 100%` because it is wrong if the parent has padding. */
.uk-position-top {
  top: 0;
  left: 0;
  right: 0;
}
.uk-position-bottom {
  bottom: 0;
  left: 0;
  right: 0;
}
.uk-position-top-left {
  top: 0;
  left: 0;
}
.uk-position-top-right {
  top: 0;
  right: 0;
}
.uk-position-bottom-left {
  bottom: 0;
  left: 0;
}
.uk-position-bottom-right {
  bottom: 0;
  right: 0;
}
/*
 * Cover
 */
.uk-position-cover {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
/*
 * Relative
 */
.uk-position-relative {
  position: relative !important;
}
/*
 * Z-index
 */
.uk-position-z-index {
  z-index: 1;
}
/* Display
 ========================================================================== */
/*
 * Display
 * 1. Required if child is a responsive image
 */
.uk-display-block {
  display: block !important;
}
.uk-display-inline {
  display: inline !important;
}
.uk-display-inline-block {
  display: inline-block !important;
  /* 1 */
  max-width: 100%;
}
/*
 * Visibility
 * Avoids setting display to `block` so it works also with `inline-block` and `table`
 */
/* Desktop and bigger */
@media (min-width: 960px) {
  .uk-visible-small {
    display: none !important;
  }
  .uk-visible-medium {
    display: none !important;
  }
  .uk-hidden-large {
    display: none !important;
  }
}
/* Tablets portrait */
@media (min-width: 768px) and (max-width: 959px) {
  .uk-visible-small {
    display: none !important;
  }
  .uk-visible-large {
    display: none !important ;
  }
  .uk-hidden-medium {
    display: none !important;
  }
}
/* Phone landscape and smaller*/
@media (max-width: 767px) {
  .uk-visible-medium {
    display: none !important;
  }
  .uk-visible-large {
    display: none !important;
  }
  .uk-hidden-small {
    display: none !important;
  }
}
/* Remove from the flow and screen readers on any device */
.uk-hidden {
  display: none !important;
  visibility: hidden !important;
}
/* It's hidden, but still affects layout */
.uk-invisible {
  visibility: hidden !important;
}
/* Show on hover */
.uk-visible-hover:hover .uk-hidden,
.uk-visible-hover:hover .uk-invisible {
  display: block !important;
  visibility: visible !important;
}
.uk-visible-hover-inline:hover .uk-hidden,
.uk-visible-hover-inline:hover .uk-invisible {
  display: inline-block !important;
  visibility: visible !important;
}
/* Hide on touch */
.uk-touch .uk-hidden-touch,
.uk-notouch .uk-hidden-notouch {
  display: none !important;
}
/* ========================================================================
   Component: Flex
 ========================================================================== */
.uk-flex {
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
}
.uk-flex-inline {
  display: -ms-inline-flexbox;
  display: -webkit-inline-flex;
  display: inline-flex;
}
/*
 * Fixes initial flex-shrink value in IE10
 */
.uk-flex > *,
.uk-flex-inline > * {
  -ms-flex-negative: 1;
}
/* Alignment
 ========================================================================== */
/*
 * Vertical alignment
 * Default value is `stretch`
 */
.uk-flex-top {
  -ms-flex-align: start;
  -webkit-align-items: flex-start;
  align-items: flex-start;
}
.uk-flex-middle {
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}
.uk-flex-bottom {
  -ms-flex-align: end;
  -webkit-align-items: flex-end;
  align-items: flex-end;
}
/*
 * Horizontal alignment
 * Default value is `flex-start`
 */
.uk-flex-center {
  -ms-flex-pack: center;
  -webkit-justify-content: center;
  justify-content: center;
}
.uk-flex-right {
  -ms-flex-pack: end;
  -webkit-justify-content: flex-end;
  justify-content: flex-end;
}
.uk-flex-space-between {
  -ms-flex-pack: justify;
  -webkit-justify-content: space-between;
  justify-content: space-between;
}
.uk-flex-space-around {
  -ms-flex-pack: distribute;
  -webkit-justify-content: space-around;
  justify-content: space-around;
}
/* Direction
 ========================================================================== */
.uk-flex-row-reverse {
  -ms-flex-direction: row-reverse;
  -webkit-flex-direction: row-reverse;
  flex-direction: row-reverse;
}
.uk-flex-column {
  -ms-flex-direction: column;
  -webkit-flex-direction: column;
  flex-direction: column;
}
.uk-flex-column-reverse {
  -ms-flex-direction: column-reverse;
  -webkit-flex-direction: column-reverse;
  flex-direction: column-reverse;
}
/* Wrap
 ========================================================================== */
.uk-flex-nowrap {
  -ms-flex-wrap: nowrap;
  -webkit-flex-wrap: nowrap;
  flex-wrap: nowrap;
}
.uk-flex-wrap {
  -ms-flex-wrap: wrap;
  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;
}
.uk-flex-wrap-reverse {
  -ms-flex-wrap: wrap-reverse;
  -webkit-flex-wrap: wrap-reverse;
  flex-wrap: wrap-reverse;
}
/*
 * Horizontal alignment
 * Default value is `stretch`
 */
.uk-flex-wrap-top {
  -ms-flex-line-pack: start;
  -webkit-align-content: flex-start;
  align-content: flex-start;
}
.uk-flex-wrap-middle {
  -ms-flex-line-pack: center;
  -webkit-align-content: center;
  align-content: center;
}
.uk-flex-wrap-bottom {
  -ms-flex-line-pack: end;
  -webkit-align-content: flex-end;
  align-content: flex-end;
}
.uk-flex-wrap-space-between {
  -ms-flex-line-pack: justify;
  -webkit-align-content: space-between;
  align-content: space-between;
}
.uk-flex-wrap-space-around {
  -ms-flex-line-pack: distribute;
  -webkit-align-content: space-around;
  align-content: space-around;
}
/* Item ordering
 ========================================================================== */
/*
 * Default is 0
 */
.uk-flex-order-first {
  -ms-flex-order: -1;
  -webkit-order: -1;
  order: -1;
}
.uk-flex-order-last {
  -ms-flex-order: 99;
  -webkit-order: 99;
  order: 99;
}
/* Phone landscape and bigger */
@media (min-width: 480px) {
  .uk-flex-order-first-small {
    -ms-flex-order: -1;
    -webkit-order: -1;
    order: -1;
  }
  .uk-flex-order-last-small {
    -ms-flex-order: 99;
    -webkit-order: 99;
    order: 99;
  }
}
/* Tablet and bigger */
@media (min-width: 768px) {
  .uk-flex-order-first-medium {
    -ms-flex-order: -1;
    -webkit-order: -1;
    order: -1;
  }
  .uk-flex-order-last-medium {
    -ms-flex-order: 99;
    -webkit-order: 99;
    order: 99;
  }
}
/* Desktop and bigger */
@media (min-width: 960px) {
  .uk-flex-order-first-large {
    -ms-flex-order: -1;
    -webkit-order: -1;
    order: -1;
  }
  .uk-flex-order-last-large {
    -ms-flex-order: 99;
    -webkit-order: 99;
    order: 99;
  }
}
/* Large screen and bigger */
@media (min-width: 1220px) {
  .uk-flex-order-first-xlarge {
    -ms-flex-order: -1;
    -webkit-order: -1;
    order: -1;
  }
  .uk-flex-order-last-xlarge {
    -ms-flex-order: 99;
    -webkit-order: 99;
    order: 99;
  }
}
/* Item dimensions
 ========================================================================== */
/*
 * Initial: 0 1 auto
 * Content dimensions, but shrinks
 */
/*
 * No Flex: 0 0 auto
 * Content dimensions
 */
.uk-flex-item-none {
  -ms-flex: none;
  -webkit-flex: none;
  flex: none;
}
/*
 * Relative Flex: 1 1 auto
 * Space is allocated considering content
 * 1. Fixes flex-shrink value in IE10
 */
.uk-flex-item-auto {
  -ms-flex: auto;
  -webkit-flex: auto;
  flex: auto;
  /* 1 */
  -ms-flex-negative: 1;
}
/*
 * Absolute Flex: 1 1 0%
 * Space is allocated solely based on flex
 */
.uk-flex-item-1 {
  -ms-flex: 1;
  -webkit-flex: 1;
  flex: 1;
}
/* ========================================================================
   Component: Contrast
 ========================================================================== */
.uk-contrast {
  color: #fff;
  /* Active */
}
.uk-contrast a:not([class]),
.uk-contrast .uk-link {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
}
.uk-contrast a:not([class]):hover,
.uk-contrast .uk-link:hover {
  color: #fff;
  text-decoration: underline;
}
.uk-contrast :not(pre) > code,
.uk-contrast :not(pre) > kbd,
.uk-contrast :not(pre) > samp {
  color: #fff;
  border-color: rgba(255, 255, 255, 0.2);
  background: rgba(255, 255, 255, 0.1);
}
.uk-contrast em {
  color: #fff;
}
.uk-contrast h1,
.uk-contrast h2,
.uk-contrast h3,
.uk-contrast h4,
.uk-contrast h5,
.uk-contrast h6 {
  color: #fff;
}
.uk-contrast hr {
  border-top-color: rgba(255, 255, 255, 0.2);
}
.uk-contrast .uk-nav li > a,
.uk-contrast .uk-nav li > a:hover {
  text-decoration: none;
}
.uk-contrast .uk-nav-side > li > a {
  color: #fff;
}
.uk-contrast .uk-nav-side > li > a:hover,
.uk-contrast .uk-nav-side > li > a:focus {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  text-shadow: none;
}
.uk-contrast .uk-nav-side > li.uk-active > a {
  background: #fff;
  color: #444;
  text-shadow: none;
}
.uk-contrast .uk-nav-side .uk-nav-header {
  color: #fff;
}
.uk-contrast .uk-nav-side .uk-nav-divider {
  border-top-color: rgba(255, 255, 255, 0.2);
}
.uk-contrast .uk-nav-side ul a {
  color: rgba(255, 255, 255, 0.7);
}
.uk-contrast .uk-nav-side ul a:hover {
  color: #fff;
}
.uk-contrast .uk-subnav > * > a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
}
.uk-contrast .uk-subnav > * > a:hover,
.uk-contrast .uk-subnav > * > a:focus {
  color: #fff;
  text-decoration: none;
}
.uk-contrast .uk-subnav > .uk-active > a {
  color: #fff;
}
.uk-contrast .uk-subnav-line > :nth-child(n+2):before {
  border-left-color: rgba(255, 255, 255, 0.2);
}
.uk-contrast .uk-subnav-pill > * > a:hover,
.uk-contrast .uk-subnav-pill > * > a:focus {
  background: rgba(255, 255, 255, 0.7);
  color: #444;
  text-decoration: none;
}
.uk-contrast .uk-subnav-pill > .uk-active > a {
  background: #fff;
  color: #444;
}
.uk-contrast .uk-tab {
  border-bottom-color: rgba(255, 255, 255, 0.2);
}
.uk-contrast .uk-tab > li > a {
  border-color: transparent;
  color: rgba(255, 255, 255, 0.7);
  text-shadow: none;
}
.uk-contrast .uk-tab > li > a:hover,
.uk-contrast .uk-tab > li > a:focus,
.uk-contrast .uk-tab > li.uk-open > a {
  border-color: rgba(255, 255, 255, 0.7);
  background: rgba(255, 255, 255, 0.7);
  color: #444;
  text-decoration: none;
}
.uk-contrast .uk-tab > li.uk-active > a {
  border-color: rgba(255, 255, 255, 0.2);
  border-bottom-color: transparent;
  background: #fff;
  color: #444;
}
.uk-contrast .uk-tab-center {
  border-bottom-color: rgba(255, 255, 255, 0.2);
}
.uk-contrast .uk-tab-grid:before {
  border-top-color: rgba(255, 255, 255, 0.2);
}
.uk-contrast .uk-list-line > li:nth-child(n+2) {
  border-top-color: rgba(255, 255, 255, 0.2);
}
.uk-contrast .uk-form select,
.uk-contrast .uk-form textarea,
.uk-contrast .uk-form input:not([type]),
.uk-contrast .uk-form input[type="text"],
.uk-contrast .uk-form input[type="password"],
.uk-contrast .uk-form input[type="datetime"],
.uk-contrast .uk-form input[type="datetime-local"],
.uk-contrast .uk-form input[type="date"],
.uk-contrast .uk-form input[type="month"],
.uk-contrast .uk-form input[type="time"],
.uk-contrast .uk-form input[type="week"],
.uk-contrast .uk-form input[type="number"],
.uk-contrast .uk-form input[type="email"],
.uk-contrast .uk-form input[type="url"],
.uk-contrast .uk-form input[type="search"],
.uk-contrast .uk-form input[type="tel"],
.uk-contrast .uk-form input[type="color"] {
  border-color: rgba(255, 255, 255, 0.8);
  background: rgba(255, 255, 255, 0.8);
  color: #444;
  background-clip: padding-box;
}
.uk-contrast .uk-form select:focus,
.uk-contrast .uk-form textarea:focus,
.uk-contrast .uk-form input:not([type]):focus,
.uk-contrast .uk-form input[type="text"]:focus,
.uk-contrast .uk-form input[type="password"]:focus,
.uk-contrast .uk-form input[type="datetime"]:focus,
.uk-contrast .uk-form input[type="datetime-local"]:focus,
.uk-contrast .uk-form input[type="date"]:focus,
.uk-contrast .uk-form input[type="month"]:focus,
.uk-contrast .uk-form input[type="time"]:focus,
.uk-contrast .uk-form input[type="week"]:focus,
.uk-contrast .uk-form input[type="number"]:focus,
.uk-contrast .uk-form input[type="email"]:focus,
.uk-contrast .uk-form input[type="url"]:focus,
.uk-contrast .uk-form input[type="search"]:focus,
.uk-contrast .uk-form input[type="tel"]:focus,
.uk-contrast .uk-form input[type="color"]:focus {
  border-color: #fff;
  background: #fff;
  color: #444;
}
.uk-contrast .uk-form :-ms-input-placeholder {
  color: rgba(68, 68, 68, 0.7) !important;
}
.uk-contrast .uk-form ::-moz-placeholder {
  color: rgba(68, 68, 68, 0.7);
}
.uk-contrast .uk-form ::-webkit-input-placeholder {
  color: rgba(68, 68, 68, 0.7);
}
.uk-contrast .uk-button {
  color: #444;
  background: #fff;
  border-color: transparent;
}
.uk-contrast .uk-button:hover,
.uk-contrast .uk-button:focus {
  background-color: rgba(255, 255, 255, 0.8);
  color: #444;
  border-color: transparent;
}
.uk-contrast .uk-button:active,
.uk-contrast .uk-button.uk-active {
  background-color: rgba(255, 255, 255, 0.7);
  color: #444;
  box-shadow: none;
}
.uk-contrast .uk-button-primary {
  background-color: #009dd8;
  color: #fff;
}
.uk-contrast .uk-button-primary:hover,
.uk-contrast .uk-button-primary:focus {
  background-color: #00aff2;
  color: #fff;
}
.uk-contrast .uk-button-primary:active,
.uk-contrast .uk-button-primary.uk-active {
  background-color: #008abf;
  color: #fff;
}
.uk-contrast .uk-icon-hover {
  color: rgba(255, 255, 255, 0.7);
}
.uk-contrast .uk-icon-hover:hover {
  color: #fff;
}
.uk-contrast .uk-icon-button {
  background: #fff;
  color: #444;
  border-color: transparent;
}
.uk-contrast .uk-icon-button:hover,
.uk-contrast .uk-icon-button:focus {
  background-color: rgba(255, 255, 255, 0.8);
  color: #444;
  border-color: transparent;
}
.uk-contrast .uk-icon-button:active {
  background-color: rgba(255, 255, 255, 0.7);
  color: #444;
  box-shadow: none;
}
.uk-contrast .uk-text-muted {
  color: rgba(255, 255, 255, 0.6) !important;
}
.uk-contrast .uk-text-primary {
  color: #2d7091 !important;
}
/* ========================================================================
   Component: Print
 ========================================================================== */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: black !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  @page {
    margin: 0.5cm;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
}


""".strip()
# end of CSS_UIKIT_2_27_1_STYLE_OFFLINE

HTML_UIKIT_2_27_1_STYLE_OFFLINE = """
<style>
{}
</style>
""".format(CSS_UIKIT_2_27_1_STYLE_OFFLINE)

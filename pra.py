@charset "UTF-8";
/***** Normalize.css *****/
/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */
html {
  line-height: 1.15;
  -webkit-text-size-adjust: 100%;
}

body {
  margin: 0;
}

main {
  display: block;
}

h1 {
  font-size: 2em;
  margin: 0.67em 0;
}

hr {
  box-sizing: content-box;
  height: 0;
  overflow: visible;
}

pre {
  font-family: monospace, monospace;
  font-size: 1em;
}

a {
  background-color: transparent;
}

abbr[title] {
  border-bottom: none;
  text-decoration: underline;
  text-decoration: underline dotted;
}

b,
strong {
  font-weight: bolder;
}

code,
kbd,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}

small {
  font-size: 80%;
}

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sub {
  bottom: -0.25em;
}

sup {
  top: -0.5em;
}

img {
  border-style: none;
}

button,
input,
optgroup,
select,
textarea {
  font-family: inherit;
  font-size: 100%;
  line-height: 1.15;
  margin: 0;
}

button,
input {
  overflow: visible;
}

button,
select {
  text-transform: none;
}

button,
[type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button;
}

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner {
  border-style: none;
  padding: 0;
}

button:-moz-focusring,
[type="button"]:-moz-focusring,
[type="reset"]:-moz-focusring,
[type="submit"]:-moz-focusring {
  outline: 1px dotted ButtonText;
}

fieldset {
  padding: 0.35em 0.75em 0.625em;
}

legend {
  box-sizing: border-box;
  color: inherit;
  display: table;
  max-width: 100%;
  padding: 0;
  white-space: normal;
}

progress {
  vertical-align: baseline;
}

textarea {
  overflow: auto;
}

[type="checkbox"],
[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button {
  height: auto;
}

[type="search"] {
  -webkit-appearance: textfield;
  outline-offset: -2px;
}

[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}

::-webkit-file-upload-button {
  -webkit-appearance: button;
  font: inherit;
}

details {
  display: block;
}

summary {
  display: list-item;
}

template {
  display: none;
}

[hidden] {
  display: none;
}

/***** Base *****/
* {
  box-sizing: border-box;
}

body {
  background-color: $background_color;
  color: $text_color;
  font-family: $text_font;
  font-size: 15px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

@media (min-width: 1024px) {
  body > main {
    min-height: 65vh;
  }
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: $heading_font;
  margin-top: 0;
}

h1 {
  font-size: 32px;
}

h2 {
  font-size: 22px;
}

h3 {
  font-size: 18px;
  font-weight: 600;
}

h4 {
  font-size: 16px;
}

a {
  color: $link_color;
  text-decoration: none;
}

a:visited {
  color: $visited_link_color;
}

a:hover, a:active, a:focus {
  text-decoration: underline;
}

input,
textarea {
  color: #000;
  font-size: 14px;
}

input {
  max-width: 100%;
  box-sizing: border-box;
  transition: border 0.12s ease-in-out;
}

input:not([type="checkbox"]) {
  outline: none;
}

input:not([type="checkbox"]):focus {
  border: 1px solid $brand_color;
}

input[disabled] {
  background-color: #ddd;
}

select {
  -webkit-appearance: none;
  -moz-appearance: none;
  background: url("data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath fill='%23CCC' d='M0 0h10L5 6 0 0z'/%3E%3C/svg%3E%0A") no-repeat #fff;
  background-position: right 10px center;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px 30px 8px 10px;
  outline: none;
  color: #555;
  width: 100%;
}

select:focus {
  border: 1px solid $brand_color;
}

select::-ms-expand {
  display: none;
}

textarea {
  border: 1px solid #ddd;
  border-radius: 2px;
  resize: vertical;
  width: 100%;
  outline: none;
  padding: 10px;
}

textarea:focus {
  border: 1px solid $brand_color;
}

.container {
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 5%;
}

@media (min-width: 1160px) {
  .container {
    padding: 0;
    width: 90%;
  }
}

.container-divider {
  border-top: 1px solid #ddd;
  margin-bottom: 20px;
}

ul {
  list-style: none;
  margin: 5px;
  padding: 5px;
  position: sticky;
}

.error-page {
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 5%;
}

@media (min-width: 1160px) {
  .error-page {
    padding: 0;
    width: 90%;
  }
}

.visibility-hidden {
  border: 0;
  clip: rect(0 0 0 0);
  -webkit-clip-path: inset(50%);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
  white-space: nowrap;
}

/***** Buttons *****/
.button, .split-button button, .section-subscribe button, .article-subscribe button, .community-follow button, .requests-table-toolbar .organization-subscribe button, .subscriptions-subscribe button, .pagination-next-link, .pagination-prev-link, .pagination-first-link, .pagination-last-link {
  background-color: transparent;
  border: 1px solid $brand_color;
  border-radius: 4px;
  color: $brand_color;
  cursor: pointer;
  display: inline-block;
  font-size: 12px;
  line-height: 2.34;
  margin: 0;
  padding: 0 20px;
  text-align: center;
  transition: background-color .12s ease-in-out, border-color .12s ease-in-out, color .15s ease-in-out;
  user-select: none;
  white-space: nowrap;
  width: 100%;
  -webkit-touch-callout: none;
}

@media (min-width: 768px) {
  .button, .split-button button, .section-subscribe button, .article-subscribe button, .community-follow button, .requests-table-toolbar .organization-subscribe button, .subscriptions-subscribe button, .pagination-next-link, .pagination-prev-link, .pagination-first-link, .pagination-last-link {
    width: auto;
  }
}

.button:visited, .split-button button:visited, .section-subscribe button:visited, .article-subscribe button:visited, .community-follow button:visited, .requests-table-toolbar .organization-subscribe button:visited, .subscriptions-subscribe button:visited, .pagination-next-link:visited, .pagination-prev-link:visited, .pagination-first-link:visited, .pagination-last-link:visited, .button:hover, .split-button button:hover, .section-subscribe button:hover, .article-subscribe button:hover, .community-follow button:hover, .requests-table-toolbar .organization-subscribe button:hover, .subscriptions-subscribe button:hover, .pagination-next-link:hover, .pagination-prev-link:hover, .pagination-first-link:hover, .pagination-last-link:hover, .button:active, .split-button button:active, .section-subscribe button:active, .article-subscribe button:active, .community-follow button:active, .requests-table-toolbar .organization-subscribe button:active, .subscriptions-subscribe button:active, .pagination-next-link:active, .pagination-prev-link:active, .pagination-first-link:active, .pagination-last-link:active, .button:focus, .split-button button:focus, .section-subscribe button:focus, .article-subscribe button:focus, .community-follow button:focus, .requests-table-toolbar .organization-subscribe button:focus, .subscriptions-subscribe button:focus, .pagination-next-link:focus, .pagination-prev-link:focus, .pagination-first-link:focus, .pagination-last-link:focus, .button.button-primary, .split-button button.button-primary, .section-subscribe button.button-primary, .section-subscribe button[data-selected="true"], .article-subscribe button.button-primary, .article-subscribe button[data-selected="true"], .community-follow button.button-primary, .requests-table-toolbar .organization-subscribe button.button-primary, .requests-table-toolbar .organization-subscribe button[data-selected="true"], .subscriptions-subscribe button.button-primary, .subscriptions-subscribe button[data-selected="true"], .button-primary.pagination-next-link, .button-primary.pagination-prev-link, .button-primary.pagination-first-link, .button-primary.pagination-last-link {
  background-color: $brand_color;
  color: $brand_text_color;
  text-decoration: none;
}

.button.button-primary:hover, .split-button button:hover, .section-subscribe button.button-primary:hover, .section-subscribe button:hover[data-selected="true"], .article-subscribe button.button-primary:hover, .article-subscribe button:hover[data-selected="true"], .community-follow button.button-primary:hover, .requests-table-toolbar .organization-subscribe button.button-primary:hover, .requests-table-toolbar .organization-subscribe button:hover[data-selected="true"], .subscriptions-subscribe button.button-primary:hover, .subscriptions-subscribe button:hover[data-selected="true"], .button-primary.pagination-next-link:hover, .button-primary.pagination-prev-link:hover, .button-primary.pagination-first-link:hover, .button-primary.pagination-last-link:hover, .button.button-primary:focus, .split-button button.button-primary:focus, .section-subscribe button.button-primary:focus, .section-subscribe button:focus[data-selected="true"], .article-subscribe button.button-primary:focus, .article-subscribe button:focus[data-selected="true"], .community-follow button.button-primary:focus, .requests-table-toolbar .organization-subscribe button.button-primary:focus, .requests-table-toolbar .organization-subscribe button:focus[data-selected="true"], .subscriptions-subscribe button.button-primary:focus, .subscriptions-subscribe button:focus[data-selected="true"], .button-primary.pagination-next-link:focus, .button-primary.pagination-prev-link:focus, .button-primary.pagination-first-link:focus, .button-primary.pagination-last-link:focus, .button.button-primary:active, .split-button button.button-primary:active, .section-subscribe button.button-primary:active, .section-subscribe button:active[data-selected="true"], .article-subscribe button.button-primary:active, .article-subscribe button:active[data-selected="true"], .community-follow button.button-primary:active, .requests-table-toolbar .organization-subscribe button.button-primary:active, .requests-table-toolbar .organization-subscribe button:active[data-selected="true"], .subscriptions-subscribe button.button-primary:active, .subscriptions-subscribe button:active[data-selected="true"], .button-primary.pagination-next-link:active, .button-primary.pagination-prev-link:active, .button-primary.pagination-first-link:active, .button-primary.pagination-last-link:active {
  background-color: darken($brand_color, 20%);
  border-color: darken($brand_color, 20%);
}

.button[data-disabled], .split-button button[data-disabled], .section-subscribe button[data-disabled], .article-subscribe button[data-disabled], .community-follow button[data-disabled], .requests-table-toolbar .organization-subscribe button[data-disabled], .subscriptions-subscribe button[data-disabled], .pagination-next-link[data-disabled], .pagination-prev-link[data-disabled], .pagination-first-link[data-disabled], .pagination-last-link[data-disabled] {
  cursor: default;
}

.button-large, input[type="submit"] {
  cursor: pointer;
  background-color: $brand_color;
  border: 0;
  border-radius: 4px;
  color: $brand_text_color;
  font-size: 14px;
  line-height: 2.72;
  min-width: 190px;
  padding: 0 1.9286em;
  width: 100%;
}

@media (min-width: 768px) {
  .button-large, input[type="submit"] {
    width: auto;
  }
}

.button-large:hover, .button-large:active, .button-large:focus, input[type="submit"]:hover, input[type="submit"]:active, input[type="submit"]:focus {
  background-color: darken($brand_color, 20%);
}

.button-large[disabled], input[type="submit"][disabled] {
  background-color: #ddd;
}

.button-secondary {
  color: lighten($text_color, 20%);
  border: 1px solid #ddd;
  background-color: transparent;
}

.button-secondary:hover, .button-secondary:focus, .button-secondary:active {
  color: $text_color;
  border: 1px solid #ddd;
  background-color: darken($background_color, 3%);
}

/***** Split button *****/
.split-button {
  display: flex;
}

.split-button button {
  background-color: $brand_color;
  border: 0;
  color: $brand_text_color;
  height: 32px;
  line-height: 16px;
  outline-color: $brand_color;
}

[dir="rtl"] .split-button button:not(:only-child):first-child {
  border-left: 1px solid $brand_text_color;
  border-top-left-radius: unset;
  border-bottom-left-radius: unset;
}

[dir="ltr"] .split-button button:not(:only-child):first-child {
  border-right: 1px solid $brand_text_color;
  border-top-right-radius: unset;
  border-bottom-right-radius: unset;
}

.split-button button:not(:only-child):last-child {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 26px;
  min-width: 26px;
  max-width: 26px;
  padding: 0;
}

[dir="rtl"] .split-button button:not(:only-child):last-child {
  border-top-right-radius: unset;
  border-bottom-right-radius: unset;
}

[dir="ltr"] .split-button button:not(:only-child):last-child {
  border-top-left-radius: unset;
  border-bottom-left-radius: unset;
}

/***** Tables *****/
.table {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
  border-spacing: 0;
}

@media (min-width: 768px) {
  .table {
    table-layout: auto;
  }
}

.table th,
.table th a {
  color: lighten($text_color, 20%);
  font-size: 13px;
  text-align: left;
}

[dir="rtl"] .table th, [dir="rtl"]
.table th a {
  text-align: right;
}

.table tr {
  border-bottom: 1px solid #ddd;
  display: block;
  padding: 20px 0;
}

@media (min-width: 768px) {
  .table tr {
    display: table-row;
  }
}

.table td {
  display: block;
}

@media (min-width: 768px) {
  .table td {
    display: table-cell;
  }
}

@media (min-width: 1024px) {
  .table td, .table th {
    padding: 20px 30px;
  }
}

@media (min-width: 768px) {
  .table td, .table th {
    padding: 10px 20px;
    height: 60px;
  }
}

/***** Forms *****/
.form {
  max-width: 650px;
}

.form-field ~ .form-field {
  margin-top: 25px;
}

.form-field label {
  display: block;
  font-size: 13px;
  margin-bottom: 5px;
}

.form-field input {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  width: 100%;
}

.form-field input:focus {
  border: 1px solid $brand_color;
}

.form-field input[type="text"] {
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-field input[type="text"]:focus {
  border: 1px solid $brand_color;
}

.form-field input[type="checkbox"] {
  width: auto;
}

.form-field .nesty-input {
  border-radius: 4px;
  height: 40px;
  line-height: 40px;
  outline: none;
  vertical-align: middle;
}

.form-field .nesty-input:focus {
  border: 1px solid $brand_color;
  text-decoration: none;
}

.form-field .hc-multiselect-toggle:focus {
  outline: none;
  border: 1px solid $brand_color;
  text-decoration: none;
}

.form-field textarea {
  vertical-align: middle;
}

.form-field input[type="checkbox"] + label {
  margin: 0 0 0 10px;
}

.form-field .optional {
  color: lighten($text_color, 20%);
  margin-left: 4px;
}

.form-field p {
  color: lighten($text_color, 20%);
  font-size: 12px;
  margin: 5px 0;
}

.form footer {
  margin-top: 40px;
  padding-top: 30px;
}

.form footer a {
  color: lighten($text_color, 20%);
  cursor: pointer;
  margin-right: 15px;
}

.form .suggestion-list {
  font-size: 13px;
  margin-top: 30px;
}

.form .suggestion-list label {
  border-bottom: 1px solid #ddd;
  display: block;
  padding-bottom: 5px;
}

.form .suggestion-list li {
  padding: 10px 0;
}

.form .suggestion-list li a:visited {
  color: $visited_link_color;
}

/***** Header *****/
.header {
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 5%;
  position: relative;
  align-items: center;
  display: flex;
  height: 71px;
  justify-content: space-between;
}

@media (min-width: 1160px) {
  .header {
    padding: 0;
    width: 90%;
  }
}

.logo img {
  max-height: 37px;
  vertical-align: middle;
}

.logo span {
  margin: 0 10px;
  color: $brand_color;
}

.logo a {
  display: inline-block;
  margin: -40px
}

.logo a:hover, .logo a:focus, .logo a:active {
  text-decoration: none;
}

.user-nav {
  display: inline-block;
  position: absolute;
  white-space: nowrap;
}

@media (min-width: 768px) {
  .user-nav {
    position: relative;
  }
}

.user-nav[aria-expanded="true"] {
  background-color: #fff;
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.15), 0 4px 10px 0 rgba(0, 0, 0, 0.1);
  border: solid 1px #ddd;
  right: 0;
  left: 0;
  top: 71px;
  z-index: 1;
}

.user-nav[aria-expanded="true"] > a {
  display: block;
  margin: 20px;
}

.user-nav[aria-expanded="true"] > .user-nav-list li {
  display: block;
}

.user-nav[aria-expanded="true"] > .user-nav-list a {
  display: block;
  margin: 20px;
}

.user-nav-list {
  display: block;
  list-style: none;
}

.user-nav-list > li {
  display: inline-block;
}

@media (max-width: 768px) {
  .nav-wrapper-desktop {
    display: none;
  }
}

@media (min-width: 768px) {
  .nav-wrapper-desktop {
    display: none;
  }
}

@media (min-width: 1024px) {
  .nav-wrapper-desktop {
    display: inline-block;
  }
}

.nav-wrapper-desktop a {
  border: 0;
  color: $link_color;
  display: none;
  font-size: 14px;
  padding: 0 20px 0 0;
  width: auto;
}

@media (min-width: 768px) {
  .nav-wrapper-desktop a {
    display: inline-block;
  }
}

[dir="rtl"] .nav-wrapper-desktop a {
  padding: 0 0 0 20px;
}

.nav-wrapper-desktop a:hover, .nav-wrapper-desktop a:focus, .nav-wrapper-desktop a:active {
  background-color: transparent;
  color: $link_color;
  text-decoration: underline;
}

@media (min-width: 1024px) {
  .nav-wrapper-mobile {
    display: none;
  }
}

.nav-wrapper-mobile .menu-button-mobile {
  background: none;
  border: 0;
  width: auto;
  min-width: 71px;
  cursor: pointer;
}

.nav-wrapper-mobile .menu-button-mobile .icon-menu {
  padding: 7px;
  vertical-align: middle;
  width: 30px;
  height: 30px;
  border-radius: 50%;
}

.nav-wrapper-mobile .menu-button-mobile[aria-expanded="true"] .icon-menu {
  background: #f3f3f3;
}

.nav-wrapper-mobile .menu-list-mobile {
  position: absolute;
  background-color: #fff;
  box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 0.15);
  border-top: solid 1px #ddd;
  border-bottom: solid 1px #ddd;
  right: 0;
  left: 0;
  top: 71px;
  z-index: 2;
}

.nav-wrapper-mobile .menu-list-mobile[aria-expanded="false"] {
  display: none;
}

.nav-wrapper-mobile .menu-list-mobile[aria-expanded="true"] {
  display: block;
}

.nav-wrapper-mobile .menu-list-mobile-items .item {
  margin: 4px 0;
}

.nav-wrapper-mobile .menu-list-mobile-items li:empty:not(.nav-divider) {
  display: none;
}

.nav-wrapper-mobile .menu-list-mobile-items .nav-divider {
  border-bottom: 0.1px solid #ddd;
  padding: 0;
}

.nav-wrapper-mobile .menu-list-mobile-items .nav-divider:last-child {
  display: none;
}

.nav-wrapper-mobile .menu-list-mobile-items button {
  background: none;
  border: none;
  padding: 8px 24px;
  width: 100%;
  height: 100%;
  color: $text_color;
  cursor: pointer;
  text-align: start;
}

.nav-wrapper-mobile .menu-list-mobile-items button:active, .nav-wrapper-mobile .menu-list-mobile-items button:focus, .nav-wrapper-mobile .menu-list-mobile-items button:hover {
  background-color: #f3f3f3;
  text-decoration: underline;
}

.nav-wrapper-mobile .menu-list-mobile-items a {
  display: block;
  padding: 8px 24px;
  width: 100%;
  height: 100%;
  color: $text_color;
}

.nav-wrapper-mobile .menu-list-mobile-items a:active, .nav-wrapper-mobile .menu-list-mobile-items a:focus, .nav-wrapper-mobile .menu-list-mobile-items a:hover {
  background-color: #f3f3f3;
}

.nav-wrapper-mobile .menu-list-mobile-items .my-profile {
  display: flex;
  line-height: 1.5;
}

.nav-wrapper-mobile .menu-list-mobile-items .my-profile .my-profile-tooltip {
  font-size: 12px;
  color: #68737D;
}

.nav-wrapper-mobile .menu-list-mobile-items .menu-profile-avatar {
  height: 20px;
  width: 20px;
  border-radius: 50%;
  display: inline-block;
  margin-right: 8px;
  margin-top: 1px;
}

[dir="rtl"] .nav-wrapper-mobile .menu-list-mobile-items .menu-profile-avatar {
  margin-right: 0;
  margin-left: 8px;
}

.skip-navigation {
  align-items: center;
  background-color: black;
  color: white;
  display: flex;
  font-size: 14px;
  justify-content: center;
  left: -999px;
  margin: 20px;
  padding: 20px;
  overflow: hidden;
  position: absolute;
  top: auto;
  z-index: -999;
}

[dir="rtl"] .skip-navigation {
  left: initial;
  right: -999px;
}

.skip-navigation:focus, .skip-navigation:active {
  left: auto;
  overflow: auto;
  text-align: center;
  text-decoration: none;
  top: auto;
  z-index: 999;
}

[dir="rtl"] .skip-navigation:focus, [dir="rtl"] .skip-navigation:active {
  left: initial;
  right: auto;
}

/***** User info in header *****/
.user-info {
  display: inline-block;
}

.user-info .dropdown-toggle::after {
  display: none;
}

@media (min-width: 768px) {
  .user-info .dropdown-toggle::after {
    display: inline-block;
  }
}

.user-info > button {
  border: 0;
  color: $link_color;
  min-width: 0;
  padding: 0;
  white-space: nowrap;
}

.user-info > button:hover, .user-info > button:focus {
  color: $link_color;
  background-color: transparent;
}

.user-info > button::after {
  color: $link_color;
  padding-right: 15px;
}

[dir="rtl"] .user-info > button::after {
  padding-left: 15px;
  padding-right: 0;
}

#user #user-name {
  display: none;
  font-size: 14px;
}

@media (min-width: 768px) {
  #user #user-name {
    display: inline-block;
  }
}

#user #user-name:hover {
  text-decoration: underline;
}

/***** User avatar *****/
.user-avatar {
  height: 25px;
  width: 25px;
  border-radius: 50%;
  display: inline-block;
  vertical-align: middle;
}

.avatar {
  display: inline-block;
  position: relative;
}

.avatar img {
  height: 40px;
  width: 40px;
}

.avatar .icon-agent {
  color: $brand_color;
  border: 2px solid #fff;
  border-radius: 50%;
  bottom: -4px;
  background-color: $brand_text_color;
  font-size: 17px;
  height: 17px;
  line-height: 17px;
  position: absolute;
  right: -2px;
  text-align: center;
  width: 17px;
}

/***** Footer *****/
.footer {
  border-top: 1px solid #ddd;
  margin-top: 60px;
  padding: 30px 0;
}

.footer a {
  color: lighten($text_color, 20%);
}

.footer-inner {
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 5%;
  display: flex;
  justify-content: space-between;
}

@media (min-width: 1160px) {
  .footer-inner {
    padding: 0;
    width: 90%;
  }
}

.footer-language-selector button {
  color: lighten($text_color, 20%);
  display: inline-block;
}

.powered-by-zendesk a,
.powered-by-zendesk a:visited {
  color: lighten($text_color, 20%);
}

/***** Breadcrumbs *****/
.breadcrumbs {
  margin: 0 0 15px 0;
  padding: 0;
}

@media (min-width: 768px) {
  .breadcrumbs {
    margin: 0;
  }
}

.breadcrumbs li {
  color: lighten($text_color, 20%);
  display: inline;
  font-size: 13px;
  max-width: 450px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.breadcrumbs li + li::before {
  content: ">";
  margin: 0 4px;
}

.breadcrumbs li a:visited {
  color: $link_color;
}

/***** Search field *****/
.search-container {
  position: relative;
}

.search {
  border-color: #ddd;
  border-radius: 30px;
  border-style: solid;
  border-width: 1px;
  display: flex;
  position: relative;
  transition: border 0.12s ease-in-out;
}

.search:focus-within {
  border-color: $brand_color;
}

.search input[type="search"],
.search .clear-button, .btn--primary, .section-subscribe button, .lt-article-subscribe button, .lt-community-follow button, .subscriptions-subscribe button, .lt-profile__buttons button, .lt-profile__buttons a {
  background-color: #fff;
  border-radius: 30px;
  border: none;
}

.search-full input[type="search"],
.search-full .clear-button {
  border-color: #fff;
}

.search input[type="search"] {
  appearance: none;
  -webkit-appearance: none;
  box-sizing: border-box;
  color: #666;
  flex: 1 1 auto;
  height: 40px;
  width: 100%;
}

.search input[type="search"]:focus {
  color: #555;
}

.search input[type="search"]::-webkit-search-decoration, .search input[type="search"]::-webkit-search-cancel-button, .search input[type="search"]::-webkit-search-results-button, .search input[type="search"]::-webkit-search-results-decoration {
  -webkit-appearance: none;
}

.search input[type="search"]:-webkit-autofill, .search input[type="search"]:-webkit-autofill:hover, .search input[type="search"]:-webkit-autofill:focus {
  -webkit-box-shadow: 0 0 0 1000px #fff inset;
}

.search .clear-button {
  align-items: center;
  box-sizing: border-box;
  color: #777;
  cursor: pointer;
  display: none;
  flex: none;
  justify-content: center;
  padding: 0 15px;
}

.search .clear-button:hover {
  background-color: $brand_color;
  color: #fff;
}

.search .clear-button:focus {
  outline: 0;
  box-shadow: 0 0 0 3px $brand_color;
}

.search-has-value .clear-button {
  display: flex;
}

[dir="ltr"] .search input[type="search"] {
  padding-left: 40px;
  padding-right: 20px;
}

[dir="ltr"] .search-has-value input[type="search"] {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
  border-right-color: transparent;
}

[dir="ltr"] .search-has-value input[type="search"]:focus {
  border-right-color: $brand_color;
}

[dir="ltr"] .search .clear-button {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
  border-left-color: transparent;
}

[dir="ltr"] .search .clear-button:focus {
  border-left-color: $brand_color;
}

[dir="rtl"] .search input[type="search"] {
  padding-left: 20px;
  padding-right: 40px;
}

[dir="rtl"] .search-has-value input[type="search"] {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
  border-left-color: transparent;
}

[dir="rtl"] .search-has-value input[type="search"]:focus {
  border-left-color: $brand_color;
}

[dir="rtl"] .search .clear-button {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
  border-right-color: transparent;
}

[dir="rtl"] .search .clear-button:focus {
  border-right-color: $brand_color;
}

.search-icon {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  position: absolute;
  left: 15px;
  z-index: 1;
  width: 18px;
  height: 18px;
  color: #777;
  pointer-events: none;
}

[dir="rtl"] .search-icon {
  left: auto;
  right: 15px;
}

/***** Hero component *****/
.hero {
  background-image: url($homepage_background_image);
  background-position: center;
  background-size: cover;
  height: 300px;
  padding: 0 20px;
  text-align: center;
  width: 100%;
}

.hero-inner {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  max-width: 610px;
  margin: 0 auto;
}

.page-header {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 10px 0;
}

@media (min-width: 768px) {
  .page-header {
    align-items: baseline;
    flex-direction: row;
    margin: 0;
  }
}

.page-header .section-subscribe {
  flex-shrink: 0;
  margin-bottom: 10px;
}

@media (min-width: 768px) {
  .page-header .section-subscribe {
    margin-bottom: 0;
  }
}

.page-header h1 {
  flex-grow: 1;
  margin-bottom: 10px;
}

.page--description {
  font-style: italic;
  margin: 0 0 30px 0;
  word-break: break-word;
}

@media (min-width: 1024px) {
  .page-header-description {
    flex-basis: 100%;
  }
}

.page-header .icon-lock {
  height: 20px;
  width: 20px;
  position: relative;
  left: -5px;
  vertical-align: baseline;
}

.sub-nav {
  align-items: baseline;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  gap: 15px 30px;
  justify-content: space-between;
  margin-bottom: 55px;
}

@media (min-width: 768px) {
  .sub-nav {
    flex-direction: row;
  }
}

.sub-nav .breadcrumbs {
  margin: 0;
}

.sub-nav .search-container {
  max-width: 300px;
  width: 100%;
}

@media (min-width: 768px) {
  .sub-nav .search-container {
    flex: 0 1 300px;
  }
}

.sub-nav input[type="search"]::after {
  font-size: 15px;
}

/***** Blocks *****/
/* Used in Homepage#categories and Community#topics */
.blocks-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  list-style: none;
  padding: 0;
}

@media (min-width: 768px) {
  .blocks-list {
    margin: 0 -15px;
  }
}

.blocks-item {
  border: 1px solid $brand_color;
  border-radius: 4px;
  box-sizing: border-box;
  color: $brand_color;
  display: flex;
  flex: 1 0 340px;
  margin: 0 0 30px;
  max-width: 100%;
  text-align: center;
}

@media (min-width: 768px) {
  .blocks-item {
    margin: 0 15px 30px;
  }
}

.blocks-item:hover, .blocks-item:focus, .blocks-item:active {
  background-color: $brand_color;
}

.blocks-item:hover *, .blocks-item:focus *, .blocks-item:active * {
  color: $brand_text_color;
  text-decoration: none;
}

.blocks-item-internal {
  background-color: transparent;
  border: 1px solid #ddd;
}

.blocks-item-internal .icon-lock {
  height: 15px;
  width: 15px;
  bottom: 5px;
  position: relative;
}

.blocks-item-internal a {
  color: $text_color;
}

.blocks-item-link {
  color: $brand_color;
  padding: 20px 30px;
  display: flex;
  flex-direction: column;
  flex: 1;
  justify-content: center;
  border-radius: inherit;
}

.blocks-item-link:visited, .blocks-item-link:hover, .blocks-item-link:active {
  color: inherit;
  text-decoration: none;
}

.blocks-item-link:focus {
  outline: 0;
  box-shadow: 0 0 0 3px $brand_color;
  text-decoration: none;
}

.blocks-item-title {
  margin-bottom: 0;
  font-size: 16px;
}

.blocks-item-description {
  margin: 0;
}

.blocks-item-description:not(:empty) {
  margin-top: 10px;
}

/***** Homepage *****/
.section {
  margin-bottom: 40px;
}

@media (min-width: 768px) {
  .section {
    margin-bottom: 60px;
  }
}

.home-section h2 {
  margin-bottom: 10px;
  text-align: center;
}

/***** Promoted articles *****/
.promoted-articles {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}

@media (min-width: 1024px) {
  .promoted-articles {
    flex-direction: row;
  }
}

.promoted-articles-item {
  flex: 1 0 auto;
}

@media (min-width: 1024px) {
  .promoted-articles-item {
    align-self: flex-end;
    flex: 0 0 auto;
    padding-right: 30px;
    width: 33%;
    /* Three columns on desktop */
  }
  [dir="rtl"] .promoted-articles-item {
    padding: 0 0 0 30px;
  }
}

.promoted-articles-item:nth-child(3n) {
  padding-right: 0;
}

.promoted-articles-item a {
  display: block;
  border-bottom: 1px solid #ddd;
  padding: 15px 0;
}

.promoted-articles-item .icon-lock {
  vertical-align: baseline;
}

.promoted-articles-item:last-child a {
  border: 0;
}

@media (min-width: 1024px) {
  .promoted-articles-item:last-child a {
    border-bottom: 1px solid #ddd;
  }
}

/***** Community section in homepage *****/
.community {
  text-align: center;
}

.community-image {
  min-height: 300px;
  margin-top: 32px;
  background-image: url($community_image);
  background-position: center;
  background-repeat: no-repeat;
  max-width: 100%;
}

.community a {
  color: $link_color;
  text-decoration: underline;
}

.community a:visited {
  color: $visited_link_color;
}

.community a:hover, .community a:active, .community a:focus {
  color: $hover_link_color;
}

.community,
.activity {
  border-top: 1px solid #ddd;
  padding: 30px 0;
}

/***** Recent activity *****/
.recent-activity-header {
  margin-bottom: 10px;
  text-align: center;
}

.recent-activity-list {
  padding: 0;
}

.recent-activity-item {
  border-bottom: 1px solid #ddd;
  overflow: auto;
  padding: 20px 0;
}

.recent-activity-item-parent {
  font-size: 16px;
  font-weight: 600;
}

.recent-activity-item-parent, .recent-activity-item-link {
  margin: 6px 0;
  display: inline-block;
  width: 100%;
}

@media (min-width: 768px) {
  .recent-activity-item-parent, .recent-activity-item-link {
    width: 70%;
    margin: 0;
  }
}

.recent-activity-item-link {
  font-size: 14px;
}

.recent-activity-item-meta {
  color: $text_color;
  margin: 15px 0 0 0;
  float: none;
}

@media (min-width: 768px) {
  .recent-activity-item-meta {
    margin: 0;
    float: right;
  }
  [dir="rtl"] .recent-activity-item-meta {
    float: left;
  }
}

.recent-activity-item-time, .recent-activity-item-comment {
  display: inline-block;
  font-size: 13px;
}

.recent-activity-item-comment {
  padding-left: 5px;
}

[dir="rtl"] .recent-activity-item-comment {
  padding: 0 5px 0 0;
}

.recent-activity-item-comment::before {
  display: inline-block;
}

.recent-activity-controls {
  padding-top: 15px;
}

.recent-activity-controls a {
  color: $link_color;
  text-decoration: underline;
}

.recent-activity-controls a:visited {
  color: $visited_link_color;
}

.recent-activity-controls a:hover, .recent-activity-controls a:active, .recent-activity-controls a:focus {
  color: $hover_link_color;
}

.recent-activity-accessibility-label {
  border: 0;
  clip: rect(0 0 0 0);
  -webkit-clip-path: inset(50%);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
  white-space: nowrap;
}

.recent-activity-comment-icon svg {
  vertical-align: middle;
  color: $brand_color;
  width: 16px;
  height: 16px;
}

.recent-activity-comment-icon:after {
  content: attr(data-comment-count);
  margin-left: 3px;
}

[dir="rtl"] .recent-activity-comment-icon:after {
  margin-left: 0;
  margin-right: 3px;
}

/***** Category pages *****/
.category-container {
  display: flex;
  justify-content: flex-end;
}

.category-content {
  flex: 1;
}

@media (min-width: 1024px) {
  .category-content {
    flex: 0 0 80%;
  }
}

.section-tree {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
}

@media (min-width: 768px) {
  .section-tree {
    flex-direction: row;
  }
}

.section-tree .section {
  flex: initial;
}

@media (min-width: 768px) {
  .section-tree .section {
    flex: 0 0 45%;
    /* Two columns for tablet and desktop. Leaving 5% separation between columns */
  }
}

.section-tree-title {
  margin-bottom: 0;
  font-size: 18px;
  font-weight: 600;
}

.section-tree-title a {
  color: $text_color;
}

.section-tree .see-all-articles {
  display: block;
  padding: 15px 0;
}

.article-list-item {
  font-size: 16px;
  padding: 15px 0;
}

.article-list-item a {
  color: $text_color;
}

.icon-star {
  color: $brand_color;
  font-size: 18px;
}

/***** Section pages *****/
.section-container {
  display: flex;
  justify-content: flex-end;
}

.section-content {
  flex: 1;
}

@media (min-width: 1024px) {
  .section-content {
    flex: 0 0 80%;
  }
}

.section-list {
  margin: 40px 0;
}

.section-list-item {
  border-bottom: 1px solid #ddd;
  font-size: 16px;
  padding: 15px 0;
}

.section-list-item:first-child {
  border-top: 1px solid #ddd;
}

.section-list-item a {
  align-items: center;
  color: $text_color;
  display: flex;
  justify-content: space-between;
}

.see-all-sections-trigger {
  cursor: pointer;
  display: block;
  padding: 15px;
  text-align: center;
}

.see-all-sections-trigger[aria-hidden="true"] {
  display: none;
}

/***** Article *****/
.article {
  /*
  * The article grid is defined this way to optimize readability:
  * Sidebar | Content | Free space
  * 17%     | 66%     | 17%
  */
  flex: 1 0 auto;
}

@media (min-width: 1024px) {
  .article {
    flex: 1 0 66%;
    max-width: 66%;
    min-width: 640px;
    padding: 0 30px;
  }
}

.article-container {
  display: flex;
  flex-direction: column;
}

@media (min-width: 1024px) {
  .article-container {
    flex-direction: row;
  }
}

.article-header {
  align-items: flex-start;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-bottom: 40px;
  margin-top: 20px;
}

@media (min-width: 768px) {
  .article-header {
    flex-direction: row;
    margin-top: 0;
  }
}

.article-avatar {
  margin-right: 10px;
}

.article-author {
  margin-bottom: 10px;
}

@media (min-width: 768px) {
  .article-title {
    flex-basis: 100%;
    /* Take entire row */
  }
}

.article-title .icon-lock {
  position: relative;
  left: -5px;
  vertical-align: baseline;
}

.article [role="button"] {
  flex-shrink: 0;
  /*Avoid collapsing elements in Safari (https://github.com/philipwalton/flexbugs#1-minimum-content-sizing-of-flex-items-not-honored)*/
  width: 100%;
}

@media (min-width: 768px) {
  .article [role="button"] {
    width: auto;
  }
}

.article-info {
  max-width: 100%;
}

.article-meta {
  display: inline-block;
  vertical-align: middle;
}

.article-body a {
  color: $link_color;
  text-decoration: underline;
}

.article-body a:visited {
  color: $visited_link_color;
}

.article-body a:hover, .article-body a:active, .article-body a:focus {
  color: $hover_link_color;
}

.article-body img {
  height: auto;
  max-width: 100%;
}

.article-body ul,
.article-body ol {
  padding-left: 20px;
  list-style-position: outside;
  margin: 20px 0 20px 20px;
}

[dir="rtl"] .article-body ul, [dir="rtl"]
.article-body ol {
  padding-right: 20px;
  padding-left: 0;
  margin-left: 0;
  margin-right: 20px;
}

.article-body ul > ul,
.article-body ol > ol,
.article-body ol > ul,
.article-body ul > ol,
.article-body li > ul,
.article-body li > ol {
  margin: 0;
}

.article-body ul {
  list-style-type: disc;
}

.article-body code {
  background: darken($background_color, 3%);
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 0 5px;
  margin: 0 2px;
}

.article-body pre {
  background: darken($background_color, 3%);
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 10px 15px;
  overflow: auto;
  white-space: pre;
}

.article-body blockquote {
  border-left: 1px solid #ddd;
  color: lighten($text_color, 20%);
  font-style: italic;
  padding: 0 15px;
}

.article-body > p:last-child {
  margin-bottom: 0;
}

.article-content {
  line-height: 1.6;
  margin: 40px 0;
  word-wrap: break-word;
}

.article-footer {
  align-items: center;
  display: flex;
  justify-content: space-between;
  padding-bottom: 20px;
}

.article-comment-count {
  color: lighten($text_color, 20%);
}

.article-comment-count:hover {
  text-decoration: none;
}

.article-comment-count-icon {
  vertical-align: middle;
  color: $brand_color;
  width: 18px;
  height: 18px;
}

.article-sidebar {
  border-bottom: 1px solid #ddd;
  border-top: 1px solid #ddd;
  flex: 1 0 auto;
  margin-bottom: 20px;
  padding: 0;
}

@media (min-width: 1024px) {
  .article-sidebar {
    border: 0;
    flex: 0 0 17%;
    height: auto;
  }
}

.article-relatives {
  border-top: 1px solid #ddd;
  display: flex;
  flex-direction: column;
  padding: 20px 0;
}

@media (min-width: 768px) {
  .article-relatives {
    flex-direction: row;
  }
}

.article-relatives > * {
  flex: 1 0 50%;
  min-width: 50%;
  overflow-wrap: break-word;
  margin-right: 0;
}

.article-relatives > *:last-child {
  padding: 0;
}

@media (min-width: 768px) {
  .article-relatives > * {
    padding-right: 20px;
  }
}

.article-votes {
  border-top: 1px solid #ddd;
  padding: 30px 0;
  text-align: center;
}

.article-vote {
  margin: 10px 5px;
  min-width: 90px;
  width: auto;
}

.article-more-questions {
  margin: 10px 0 20px;
  text-align: center;
}

.article-more-questions a {
  color: $link_color;
  text-decoration: underline;
}

.article-more-questions a:visited {
  color: $visited_link_color;
}

.article-more-questions a:hover, .article-more-questions a:active, .article-more-questions a:focus {
  color: $hover_link_color;
}

.article-return-to-top {
  border-top: 1px solid #ddd;
}

@media (min-width: 1024px) {
  .article-return-to-top {
    display: none;
  }
}

.article-return-to-top a {
  color: $text_color;
  display: block;
  padding: 20px 0;
}

.article-return-to-top a:hover, .article-return-to-top a:focus {
  text-decoration: none;
}

.article-return-to-top-icon {
  transform: rotate(0.5turn);
}

.sidenav-title {
  font-size: 15px;
  position: relative;
  font-weight: 600;
}

.sidenav-item {
  display: block;
  margin-top: 10px;
  margin-bottom: 16px;
}

.recent-articles li,
.related-articles li {
  margin-bottom: 15px;
}

/***** Attachments *****/
/* Styles attachments inside posts, articles and comments */
.attachments .attachment-item {
  padding-left: 20px;
  position: relative;
  margin-bottom: 10px;
}

.attachments .attachment-item:last-child {
  margin-bottom: 0;
}

.attachments .attachment-item .attachment-icon {
  color: $text_color;
  left: 0;
  position: absolute;
  top: 5px;
}

[dir="rtl"] .attachments .attachment-item {
  padding-left: 0;
  padding-right: 20px;
}

[dir="rtl"] .attachments .attachment-item .attachment-icon {
  left: auto;
  right: 0;
}

.upload-dropzone span {
  color: lighten($text_color, 20%);
}

/***** Social share links *****/
.share {
  padding: 0;
  white-space: nowrap;
}

.share li, .share a {
  display: inline-block;
}

.share li {
  height: 25px;
  width: 25px;
}

.share a {
  color: lighten($text_color, 20%);
}

.share a:hover {
  text-decoration: none;
  color: $brand_color;
}

.share a svg {
  height: 18px;
  width: 18px;
  display: block;
}

/***** Comments *****/
/* Styles comments inside articles, posts and requests */
.comment {
  border-bottom: 1px solid #ddd;
  padding: 20px 0;
}

.comment-heading, .recent-articles-title,
.related-articles-title {
  margin-bottom: 5px;
  margin-top: 0;
  font-size: 18px;
  font-weight: 600;
}

.comment-overview {
  border-bottom: 1px solid #ddd;
  border-top: 1px solid #ddd;
  padding: 20px 0;
}

.comment-overview p {
  margin-top: 0;
}

.comment-callout {
  color: lighten($text_color, 20%);
  display: inline-block;
  font-size: 13px;
  margin-bottom: 0;
}

.comment-callout a {
  color: $link_color;
  text-decoration: underline;
}

.comment-callout a:visited {
  color: $visited_link_color;
}

.comment-callout a:hover, .comment-callout a:active, .comment-callout a:focus {
  color: $hover_link_color;
}

.comment-sorter {
  display: inline-block;
  float: right;
}

.comment-sorter .dropdown-toggle {
  color: lighten($text_color, 20%);
  font-size: 13px;
}

[dir="rtl"] .comment-sorter {
  float: left;
}

.comment-wrapper {
  display: flex;
  position: relative;
}

.comment-wrapper.comment-official {
  border: 1px solid $brand_color;
  padding: 40px 20px 20px;
}

@media (min-width: 768px) {
  .comment-wrapper.comment-official {
    padding-top: 20px;
  }
}

.comment-info {
  min-width: 0;
  padding-right: 20px;
  width: 100%;
}

[dir="rtl"] .comment-info {
  padding-right: 0;
  padding-left: 20px;
}

.comment-author {
  align-items: flex-end;
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

@media (min-width: 768px) {
  .comment-author {
    justify-content: space-between;
  }
}

.comment-avatar {
  margin-right: 10px;
}

[dir="rtl"] .comment-avatar {
  margin-left: 10px;
  margin-right: 0;
}

.comment-meta {
  flex: 1 0 auto;
}

.comment-labels {
  flex-basis: 100%;
}

@media (min-width: 768px) {
  .comment-labels {
    flex-basis: auto;
  }
}

.comment .status-label:not(.status-label-official) {
  margin-top: 10px;
}

@media (min-width: 768px) {
  .comment .status-label:not(.status-label-official) {
    margin-top: 0;
  }
}

.comment-form {
  display: flex;
  padding-top: 30px;
  word-wrap: break-word;
}

.comment-container {
  width: 100%;
}

.comment-form-controls {
  display: none;
  margin-top: 10px;
  text-align: left;
}

@media (min-width: 768px) {
  [dir="ltr"] .comment-form-controls {
    text-align: right;
  }
}

.comment-form-controls input[type="submit"] {
  margin-top: 15px;
}

@media (min-width: 1024px) {
  .comment-form-controls input[type="submit"] {
    margin-left: 15px;
  }
  [dir="rtl"] .comment-form-controls input[type="submit"] {
    margin-left: 0;
    margin-right: 15px;
  }
}

.comment-form-controls input[type="checkbox"] {
  margin-right: 5px;
}

.comment-form-controls input[type="checkbox"] [dir="rtl"] {
  margin-left: 5px;
}

.comment-ccs {
  display: none;
}

.comment-ccs + textarea {
  margin-top: 10px;
}

.comment-attachments {
  margin-top: 10px;
}

.comment-attachments a {
  color: $brand_color;
}

.comment-body {
  -moz-hyphens: auto;
  -ms-hyphens: auto;
  -webkit-hyphens: auto;
  word-break: break-word;
  word-wrap: break-word;
  font-family: $text_font;
  line-height: 1.6;
  overflow-x: auto;
}

.comment-body a {
  color: $link_color;
  text-decoration: underline;
}

.comment-body a:visited {
  color: $visited_link_color;
}

.comment-body a:hover, .comment-body a:active, .comment-body a:focus {
  color: $hover_link_color;
}

.comment-body img {
  height: auto;
  max-width: 100%;
}

.comment-body ul,
.comment-body ol {
  padding-left: 20px;
  list-style-position: outside;
  margin: 20px 0 20px 20px;
}

[dir="rtl"] .comment-body ul, [dir="rtl"]
.comment-body ol {
  padding-right: 20px;
  padding-left: 0;
  margin-left: 0;
  margin-right: 20px;
}

.comment-body ul > ul,
.comment-body ol > ol,
.comment-body ol > ul,
.comment-body ul > ol,
.comment-body li > ul,
.comment-body li > ol {
  margin: 0;
}

.comment-body ul {
  list-style-type: disc;
}

.comment-body code {
  background: darken($background_color, 3%);
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 0 5px;
  margin: 0 2px;
}

.comment-body pre {
  background: darken($background_color, 3%);
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 10px 15px;
  overflow: auto;
  white-space: pre;
}

.comment-body blockquote {
  border-left: 1px solid #ddd;
  color: lighten($text_color, 20%);
  font-style: italic;
  padding: 0 15px;
}

.comment-mark-as-solved {
  display: inline-block;
}

/***** Vote *****/
/* Used in article comments, post comments and post */
.vote {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.vote a:active, .vote a:hover, .vote a:focus {
  text-decoration: none;
}

.vote-sum {
  color: lighten($text_color, 20%);
  display: block;
  margin: 3px 0;
}

[dir="rtl"] .vote-sum {
  direction: ltr;
  unicode-bidi: bidi-override;
}

.vote-up svg {
  transform: scale(1, -1);
}

.vote-up:hover,
.vote-down:hover {
  color: $brand_color;
}

.vote-up, .vote-down {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-color: transparent;
  border: none;
  color: lighten($text_color, 20%);
  cursor: pointer;
  min-height: 35px;
  min-width: 35px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.vote-voted {
  color: $brand_color;
}

.vote-voted:hover {
  color: darken($brand_color, 20%);
}

/***** Actions *****/
/* Styles admin and en user actions(edit, delete, change status) in comments and posts */
.actions {
  text-align: center;
  flex-shrink: 0;
  /*Avoid collapsing elements in Safari*/
}

.actions button {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-color: transparent;
  border: none;
  cursor: pointer;
  min-height: 35px;
  min-width: 35px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/***** Community *****/
.community-hero {
  background-image: url($community_background_image);
  margin-bottom: 10px;
}

.community-footer {
  padding-top: 50px;
  text-align: center;
}

.community-footer-title {
  font-size: 16px;
  margin-bottom: 20px;
}

.community-featured-posts .title {
  font-size: 18px;
  font-weight: 600;
}

.community-featured-posts, .community-activity {
  padding-top: 40px;
  width: 100%;
}

.community-header {
  margin-bottom: 30px;
}

.community-header .title {
  margin-bottom: 0;
  font-size: 16px;
}

.post-to-community {
  margin-top: 10px;
}

@media (min-width: 768px) {
  .post-to-community {
    margin: 0;
  }
}

/* Community topics grid */
.topics {
  max-width: none;
  width: 100%;
}

.topics-item .meta-group {
  justify-content: center;
  margin-top: 20px;
}

/* Community topic page */
.topic-header {
  border-bottom: 1px solid #ddd;
  font-size: 13px;
}

@media (min-width: 768px) {
  .topic-header {
    padding-bottom: 10px;
  }
}

.topic-header .dropdown {
  display: block;
  border-top: 1px solid #ddd;
  padding: 10px 0;
}

@media (min-width: 768px) {
  .topic-header .dropdown {
    border-top: 0;
    display: inline-block;
    margin-right: 20px;
    padding: 0;
  }
}

.no-posts-with-filter {
  margin-top: 20px;
  margin-bottom: 20px;
}

/* Topic, post and user follow button */
.community-follow {
  margin-bottom: 10px;
  width: 100%;
}

@media (min-width: 768px) {
  .community-follow {
    margin-bottom: 0;
    width: auto;
  }
}

.community-follow button {
  line-height: 30px;
  padding: 0 10px 0 15px;
  position: relative;
  width: 100%;
}

@media (min-width: 768px) {
  .community-follow button {
    width: auto;
  }
}

.community-follow button:hover {
  background-color: $brand_color;
}

.community-follow button:hover::after, .community-follow button:focus::after {
  border-color: $brand_text_color;
  color: $brand_text_color;
}

.community-follow button[data-selected="true"] {
  background-color: $brand_color;
  color: $brand_text_color;
}

.community-follow button[data-selected="true"]::after {
  border-left: 1px solid $brand_text_color;
  color: $brand_text_color;
}

.community-follow button[data-selected="true"]:hover {
  background-color: darken($brand_color, 20%);
  border-color: darken($brand_color, 20%);
}

.community-follow button::after {
  border-left: 1px solid $brand_color;
  content: attr(data-follower-count);
  color: $brand_color;
  display: inline-block;
  font-family: $heading_font;
  margin-left: 15px;
  padding-left: 10px;
  position: absolute;
  right: 10px;
}

@media (min-width: 768px) {
  .community-follow button::after {
    position: static;
  }
}

[dir="rtl"] .community-follow button::after {
  border-left: 0;
  border-right: 1px solid $brand_color;
  margin: 0 10px 0 0;
  padding: 0 10px 0 0;
}

/***** Striped list *****/
/* Used in community posts list and requests list */
.striped-list {
  padding: 0;
}

.striped-list-item {
  align-items: flex-start;
  border-bottom: 1px solid #ddd;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 20px 0;
}

@media (min-width: 768px) {
  .striped-list-item {
    align-items: center;
    flex-direction: row;
  }
}

.striped-list-info {
  flex: 2;
}

.striped-list-title {
  color: $link_color;
  margin-bottom: 10px;
  margin-right: 5px;
}

.striped-list-title:hover, .striped-list-title:focus, .striped-list-title:active {
  text-decoration: underline;
}

.striped-list-title:visited {
  color: $visited_link_color;
}

.striped-list .meta-group {
  margin: 5px 0;
}

.striped-list-count {
  color: lighten($text_color, 20%);
  font-size: 13px;
  justify-content: flex-start;
  text-transform: capitalize;
}

@media (min-width: 768px) {
  .striped-list-count {
    display: flex;
    flex: 1;
    justify-content: space-around;
  }
}

.striped-list-count-item::after {
  content: "·";
  display: inline-block;
  padding: 0 5px;
}

@media (min-width: 768px) {
  .striped-list-count-item::after {
    display: none;
  }
}

.striped-list-count-item:last-child::after {
  display: none;
}

.striped-list-number {
  text-align: center;
}

@media (min-width: 768px) {
  .striped-list-number {
    color: $text_color;
    display: block;
  }
}

/***** Status labels *****/
/* Styles labels used in posts, articles and requests */
.status-label {
  background-color: #038153;
  border-radius: 4px;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  margin-right: 2px;
  padding: 3px 10px;
  vertical-align: middle;
  white-space: nowrap;
  display: inline-block;
}

.status-label:hover, .status-label:active, .status-label:focus {
  text-decoration: none;
}

.status-label-pinned, .status-label-featured, .status-label-official {
  background-color: $brand_color;
}

.status-label-official {
  border-radius: 0;
  margin-right: 0;
  position: absolute;
  right: 0;
  text-align: center;
  top: 0;
  width: 100%;
}

@media (min-width: 768px) {
  .status-label-official {
    border-radius: 0 0 4px 4px;
    right: 30px;
    width: auto;
  }
}

[dir="rtl"] .status-label-official {
  left: 30px;
  right: auto;
}

.status-label-not-planned, .status-label-closed {
  background-color: #e9ebed;
  color: lighten($text_color, 20%);
}

.status-label-pending, .status-label-pending-moderation {
  background-color: #1f73b7;
  text-align: center;
}

.status-label-open {
  background-color: #c72a1c;
}

.status-label-solved {
  background-color: #68737d;
}

.status-label-new {
  background-color: #ffb648;
  color: #703b15;
}

.status-label-hold {
  background-color: #000;
}

.status-label-request {
  max-width: 100%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (max-width: 768px) {
  .status-label-request {
    max-width: 150px;
  }
}

/***** Post *****/
/*
* The post grid is defined this way:
* Content | Sidebar
* 70%     | 30%
*/
.post {
  flex: 1;
  margin-bottom: 10px;
}

@media (min-width: 1024px) {
  .post {
    flex: 1 0 70%;
    max-width: 70%;
  }
}

.post-container {
  display: flex;
  flex-direction: column;
}

@media (min-width: 1024px) {
  .post-container {
    flex-direction: row;
  }
}

.post-header {
  align-items: center;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-bottom: 10px;
}

@media (min-width: 768px) {
  .post-header {
    align-items: baseline;
    flex-direction: row;
  }
}

.post-header .status-label {
  vertical-align: super;
}

.post-title {
  margin-bottom: 20px;
  width: 100%;
}

@media (min-width: 768px) {
  .post-title {
    margin-bottom: 0;
    padding-right: 10px;
  }
}

.post-title h1 {
  display: inline;
  vertical-align: middle;
}

@media (min-width: 768px) {
  .post-title h1 {
    margin-right: 5px;
  }
}

.post-author {
  align-items: flex-start;
  display: flex;
  justify-content: space-between;
}

.post-avatar {
  margin-bottom: 30px;
}

.post-content {
  font-family: $text_font;
  line-height: 1.6;
  word-break: break-word;
}

.post-info-container {
  display: flex;
  margin-bottom: 40px;
}

.post-info {
  min-width: 0;
  padding-right: 20px;
  width: 100%;
}

[dir="rtl"] .post-info {
  padding-right: 0;
  padding-left: 20px;
}

.post-meta {
  display: inline-block;
  flex: 1;
  margin-left: 10px;
  vertical-align: middle;
}

[dir="rtl"] .post-meta {
  margin-left: 0;
  margin-right: 10px;
}

.post-body a {
  color: $link_color;
  text-decoration: underline;
}

.post-body a:visited {
  color: $visited_link_color;
}

.post-body a:hover, .post-body a:active, .post-body a:focus {
  color: $hover_link_color;
}

.post-body img {
  height: auto;
  max-width: 100%;
}

.post-body ul,
.post-body ol {
  padding-left: 20px;
  list-style-position: outside;
  margin: 20px 0 20px 20px;
}

[dir="rtl"] .post-body ul, [dir="rtl"]
.post-body ol {
  padding-right: 20px;
  padding-left: 0;
  margin-left: 0;
  margin-right: 20px;
}

.post-body ul > ul,
.post-body ol > ol,
.post-body ol > ul,
.post-body ul > ol,
.post-body li > ul,
.post-body li > ol {
  margin: 0;
}

.post-body ul {
  list-style-type: disc;
}

.post-body code {
  background: darken($background_color, 3%);
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 0 5px;
  margin: 0 2px;
}

.post-body pre {
  background: darken($background_color, 3%);
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 10px 15px;
  overflow: auto;
  white-space: pre;
}

.post-body blockquote {
  border-left: 1px solid #ddd;
  color: lighten($text_color, 20%);
  font-style: italic;
  padding: 0 15px;
}

.post-footer {
  align-items: center;
  display: flex;
  justify-content: space-between;
  padding-bottom: 20px;
}

.post-comment-count {
  color: lighten($text_color, 20%);
}

.post-comment-count:hover {
  text-decoration: none;
}

.post-comment-count .icon-comments {
  color: $brand_color;
  display: inline-block;
  width: 18px;
  height: 18px;
  margin: 5px;
  vertical-align: middle;
}

.post-sidebar {
  border-top: 1px solid #ddd;
  flex: 1;
  padding: 30px 0;
  text-align: center;
}

@media (min-width: 1024px) {
  .post-sidebar {
    border: 0;
    flex: 1 0 30%;
    padding: 0 0 0 50px;
    text-align: initial;
  }
  [dir="rtl"] .post-sidebar {
    padding: 0 50px 0 0;
  }
}

.post-sidebar-title {
  font-size: 18px;
  font-weight: 600;
}

.post-comments {
  margin-bottom: 20px;
}

@media (min-width: 1024px) {
  .post-comments {
    margin-bottom: 0;
  }
}

/***** Community Badges *****/
/* Styles labels used next to the authors of article comments, community posts, and community comments */
.community-badge-title {
  background-color: #04444d;
  border-radius: 4px;
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  padding: 0px 8px;
  vertical-align: top;
  white-space: nowrap;
  display: inline-flex;
  line-height: 18px;
  vertical-align: middle;
}

.profile-info .community-badge-title {
  padding: 2px 8px;
  line-height: 20px;
}

.community-badge-container-achievements {
  display: flex;
}

.community-badge-container-achievements > .community-badge-titles {
  margin-left: calc(28px - 0.5em);
}

[dir="rtl"] .community-badge-container-achievements > .community-badge-titles {
  margin-right: calc(28px - 0.5em);
}

.community-name-and-title-badges {
  display: flex;
  flex-wrap: wrap;
}

.community-badge {
  margin: 2px;
}

.community-badge-achievements {
  display: block;
  height: 16px;
  white-space: nowrap;
  width: 16px;
}

.profile-info .community-badge-achievements {
  height: 40px;
  width: 40px;
}

.community-title-badges {
  flex-basis: 100%;
  margin-top: 15px;
}

.community-badge-achievements-rest {
  font-size: 12px;
  font-weight: 600;
  line-height: 20px;
  text-align: center;
  vertical-align: top;
}

.community-badge-achievements img {
  width: 100%;
  height: 100%;
}

.community-badge-titles img {
  width: 20px;
  height: 20px;
}

.profile-info .community-badge-achievements-rest {
  line-height: 40px;
  font-size: 20px;
}

/* Navigation element that collapses on mobile */
.collapsible-nav {
  flex-direction: column;
  font-size: 14px;
  position: relative;
}

@media (min-width: 768px) {
  .collapsible-nav {
    flex-direction: row;
  }
}

.collapsible-nav-border {
  border-bottom: 1px solid #ddd;
  border-top: 1px solid #ddd;
}

@media (min-width: 768px) {
  .collapsible-nav-border {
    border-top: 0;
  }
}

.collapsible-nav-toggle {
  top: calc(45px / 2);
  transform: translateY(-50%);
  position: absolute;
  right: 0;
  padding: 0;
  border: 0;
  background: none;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

@media (min-width: 768px) {
  .collapsible-nav-toggle {
    display: none;
  }
}

[dir="rtl"] .collapsible-nav-toggle {
  left: 0;
  right: auto;
}

.collapsible-nav-toggle-icon {
  display: none;
}

.collapsible-nav-toggle[aria-expanded="false"] .chevron-icon {
  display: inline-block;
}

.collapsible-nav-toggle[aria-expanded="true"] .x-icon {
  display: inline-block;
}

.collapsible-nav-toggle:focus {
  outline: none;
  border: 1px solid $brand_color;
}

.collapsible-nav-list {
  display: flex;
  flex-direction: column;
}

@media (min-width: 768px) {
  .collapsible-nav-list {
    flex-direction: row;
  }
}

.collapsible-nav-list li {
  color: $text_color;
  line-height: 45px;
  order: 1;
}

@media (min-width: 768px) {
  .collapsible-nav-list li {
    line-height: normal;
    margin-right: 30px;
  }
  [dir="rtl"] .collapsible-nav-list li {
    margin-left: 30px;
    margin-right: 0;
  }
  .collapsible-nav-list li a {
    text-decoration: none;
    padding: 15px 0;
  }
}

.collapsible-nav-list li a {
  color: $text_color;
  display: block;
}

@media (min-width: 768px) {
  .collapsible-nav-list li:hover {
    border-bottom: 4px solid #ddd;
  }
  .collapsible-nav-list li:hover a:not([aria-current="page"]) {
    padding: 15px 0 11px 0;
    text-decoration: none;
  }
}

.collapsible-nav-list li:not([aria-selected="true"]),
.collapsible-nav-list li:not(.current) {
  display: none;
}

@media (min-width: 768px) {
  .collapsible-nav-list li:not([aria-selected="true"]),
  .collapsible-nav-list li:not(.current) {
    display: block;
  }
}

@media (min-width: 768px) {
  .collapsible-nav-list li[aria-selected="true"] {
    padding: 15px 0 11px 0;
  }
}

.collapsible-nav-list li[aria-selected="true"],
.collapsible-nav-list li.current {
  order: 0;
  position: relative;
}

@media (min-width: 768px) {
  .collapsible-nav-list li[aria-selected="true"],
  .collapsible-nav-list li.current {
    border-bottom: 4px solid $brand_color;
    order: 1;
  }
}

.collapsible-nav-list li[aria-selected="true"] a,
.collapsible-nav-list li.current a {
  color: $text_color;
}

.collapsible-nav[aria-expanded="true"] li:not([aria-selected="true"]),
.collapsible-nav[aria-expanded="true"] li:not(.current) {
  display: block;
}

/* Sidebar navigation that collapses on mobile */
.collapsible-sidebar {
  flex: 1;
  max-height: 45px;
  overflow: hidden;
  padding: 10px 0;
  position: relative;
}

@media (min-width: 1024px) {
  .collapsible-sidebar {
    max-height: none;
    padding: 0;
  }
}

.collapsible-sidebar-title {
  margin-top: 0;
}

.collapsible-sidebar-toggle {
  position: absolute;
  top: calc(45px / 2);
  transform: translateY(-50%);
  right: 0;
  padding: 0;
  border: 0;
  background: none;
  width: 25px;
  height: 25px;
  border-radius: 50%;
}

@media (min-width: 1024px) {
  .collapsible-sidebar-toggle {
    display: none;
  }
}

[dir="rtl"] .collapsible-sidebar-toggle {
  left: 0;
  right: auto;
}

.collapsible-sidebar-toggle-icon {
  display: none;
}

.collapsible-sidebar-toggle[aria-expanded="false"] .chevron-icon {
  display: inline-block;
}

.collapsible-sidebar-toggle[aria-expanded="true"] .x-icon {
  display: inline-block;
}

.collapsible-sidebar-toggle:focus {
  outline: none;
  border: 1px solid $brand_color;
}

.collapsible-sidebar-body {
  display: none;
}

@media (min-width: 1024px) {
  .collapsible-sidebar-body {
    display: block;
  }
}

.collapsible-sidebar[aria-expanded="true"] {
  max-height: none;
}

.collapsible-sidebar[aria-expanded="true"] .collapsible-sidebar-body {
  display: block;
}

/***** My activities *****/
.my-activities-nav {
  background-color: darken($background_color, 5%);
  margin-bottom: 20px;
}

.my-activities-sub-nav {
  margin-bottom: 30px;
}

.my-activities-table .striped-list-title {
  /* My activities tables */
  display: block;
  margin-bottom: 10px;
  max-width: 350px;
  white-space: normal;
}

@media (min-width: 1024px) {
  .my-activities-table .striped-list-title {
    margin-bottom: 0;
    max-width: 500px;
    min-width: 350px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
}

.my-activities-table thead {
  display: none;
}

@media (min-width: 768px) {
  .my-activities-table thead {
    display: table-header-group;
  }
}

.my-activities-table th:first-child,
.my-activities-table td:first-child {
  padding-left: 0;
}

@media (min-width: 1024px) {
  .my-activities-table th:first-child,
  .my-activities-table td:first-child {
    width: 500px;
  }
}

.my-activities-table th:last-child,
.my-activities-table td:last-child {
  padding-right: 0;
}

.my-activities-table td:not(:first-child) {
  display: none;
}

@media (min-width: 768px) {
  .my-activities-table td:not(:first-child) {
    display: table-cell;
  }
}

/* Requests table */
.requests-search {
  width: 100%;
}

.requests-table-toolbar {
  align-items: flex-end;
  display: flex;
  flex-direction: column;
}

@media (min-width: 768px) {
  .requests-table-toolbar {
    flex-direction: row;
  }
}

.requests-table-toolbar .search {
  flex: 1;
  width: 100%;
}

.requests-table-toolbar .request-table-filter {
  width: 100%;
}

@media (min-width: 768px) {
  .requests-table-toolbar .request-table-filter {
    width: auto;
  }
}

.requests-table-toolbar .request-filter {
  display: block;
}

@media (min-width: 768px) {
  .requests-table-toolbar .request-filter {
    margin: 0 0 0 30px;
  }
  [dir="rtl"] .requests-table-toolbar .request-filter {
    margin: 0 30px 0 0;
  }
}

.requests-table-toolbar .request-filter-label {
  font-size: 13px;
  margin-top: 30px;
}

@media (min-width: 768px) {
  .requests-table-toolbar .request-filter-label {
    margin-top: 0;
  }
}

.requests-table-toolbar select {
  max-height: 40px;
  margin-bottom: 30px;
  width: 100%;
}

@media (min-width: 768px) {
  .requests-table-toolbar select {
    margin-bottom: 0;
    max-width: 300px;
    width: auto;
  }
}

@media (min-width: 768px) {
  .requests-table-toolbar .organization-subscribe {
    margin-left: 10px;
  }
  [dir="rtl"] .requests-table-toolbar .organization-subscribe {
    margin: 0 10px 0 0;
  }
}

.requests-table-toolbar .organization-subscribe button {
  line-height: 40px;
  max-height: 40px;
  padding: 0 20px;
}

.requests-table-toolbar + .requests-search-info {
  margin-top: 15px;
}

.requests-table-toolbar + .requests-search-info.meta-data::after {
  content: "";
  margin: 0;
}

.requests-table-toolbar + .requests-search-info + .requests {
  margin-top: 20px;
}

.requests-table-toolbar + .requests {
  margin-top: 40px;
}

.requests .requests-table-meta {
  display: block;
}

@media (min-width: 768px) {
  .requests .requests-table-meta {
    display: none;
  }
}

.requests .requests-table thead {
  display: none;
}

@media (min-width: 768px) {
  .requests .requests-table thead {
    display: table-header-group;
  }
}

.requests .requests-table-info {
  display: block;
}

@media (min-width: 768px) {
  .requests .requests-table-info {
    display: table-cell;
    vertical-align: middle;
    width: auto;
  }
}

.requests .requests-table .requests-link {
  position: relative;
}

.requests .requests-table .requests-sort-symbol {
  position: absolute;
  left: calc(100% + 3px);
  bottom: 0;
  font-size: 10px;
}

/* Following table */
@media (min-width: 768px) {
  .subscriptions-subscribe button {
    width: auto;
  }
}

.subscriptions-table td:last-child {
  display: block;
}

@media (min-width: 768px) {
  .subscriptions-table td:last-child {
    display: table-cell;
  }
}

.subscriptions-table td:first-child {
  display: flex;
  align-items: center;
}

.subscriptions-table .user-avatar {
  margin-right: 10px;
}

.subscriptions .striped-list-title {
  display: inline-block;
  vertical-align: middle;
}

/* Contributions table */
.contributions-table td:last-child {
  color: lighten($text_color, 20%);
  font-size: 13px;
}

@media (min-width: 768px) {
  .contributions-table td:last-child {
    color: inherit;
    font-size: inherit;
    font-weight: inherit;
  }
}

.no-activities {
  color: lighten($text_color, 20%);
}

/***** Request *****/
.request-container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
}

@media (min-width: 1024px) {
  .request-container {
    align-items: flex-start;
    flex-direction: row;
  }
}

.request-container .comment-container {
  min-width: 0;
}

.request-breadcrumbs {
  margin-bottom: 40px;
}

@media (min-width: 1024px) {
  .request-breadcrumbs {
    margin-bottom: 60px;
  }
}

.request-main {
  flex: 1 0 auto;
  order: 1;
}

.request-main .comment-fields, .request-main .request-submit-comment {
  display: none;
}

.request-main .comment-fields.shown {
  display: block;
}

.request-main .request-submit-comment.shown {
  display: inline;
}

@media (min-width: 1024px) {
  .request-main {
    flex: 0 0 66%;
    order: 0;
    min-width: 0;
  }
}

.request-main .comment-form-controls {
  display: block;
}

.request-main .comment-ccs {
  display: block;
}

.request-main .comment-show-container {
  border-radius: 2px;
  border: 1px solid #ddd;
  color: lighten($text_color, 20%);
  text-align: inherit;
  padding: 8px 25px;
  width: 100%;
}

.request-main .comment-show-container.hidden {
  display: none;
}

.request-main .form-field.comment-ccs > ul {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
  border-bottom: 0;
}

.request-main .form-field.comment-ccs > ul[data-hc-focus="true"] {
  border: 1px solid $brand_color;
}

.request-main .form-field.comment-ccs > input[type="text"] {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
  border-bottom: 0;
}

.request-main .comment-ccs + textarea {
  border-top-left-radius: 0;
  border-top-right-radius: 0;
  margin-top: 0;
}

.request-main .comment-ccs + textarea:focus {
  border-top: 1px solid $brand_color;
}

.request-main input#mark_as_solved {
  display: none;
}

.request-title {
  width: 100%;
}

@media (min-width: 1024px) {
  .request-title {
    border-bottom: 1px solid #ddd;
    margin-bottom: 0;
    max-width: 66%;
    padding-bottom: 20px;
  }
}

.request-sidebar {
  border-bottom: 1px solid #ddd;
  border-top: 1px solid #ddd;
  flex: 1 0 auto;
  order: 0;
}

@media (min-width: 1024px) {
  .request-sidebar {
    background-color: darken($background_color, 3%);
    border: 0;
    font-size: 13px;
    flex: 0 0 auto;
    padding: 0 20px;
    width: 30%;
  }
}

.request-sidebar h2 {
  font-size: 15px;
  font-weight: 600;
  position: relative;
}

@media (min-width: 1024px) {
  .request-sidebar h2 {
    display: none;
  }
}

.request-details {
  border-bottom: 1px solid #ddd;
  font-size: 0;
  margin: 0;
  padding-bottom: 20px;
}

.request-details:last-child {
  border: 0;
}

.request-details dt, .request-details dd {
  display: inline-block;
  vertical-align: top;
  font-size: 13px;
  margin: 20px 0 0 0;
}

.request-details dd {
  padding: 0 10px;
  width: 60%;
}

.request-details dd::after {
  content: "\A";
  white-space: pre;
}

.request-details dt {
  color: lighten($text_color, 20%);
  width: 40%;
}

.request-details .request-collaborators {
  display: inline-block;
}

.request-attachments dt, .request-attachments dd {
  width: 100%;
}

.request-attachments dd {
  margin: 10px 0 0 0;
}

.request-form textarea {
  min-height: 120px;
}

.request-follow-up {
  padding-top: 20px;
}

/***** Pagination *****/
.pagination {
  margin: 20px 0;
  text-align: center;
}

.pagination-next, .pagination-prev, .pagination-first, .pagination-last {
  display: inline-block;
}

.pagination-first-link, .pagination-last-link {
  padding: 0 10px;
}

.pagination-first-text, .pagination-last-text {
  border: 0;
  clip: rect(0 0 0 0);
  -webkit-clip-path: inset(50%);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
  white-space: nowrap;
}

.pagination-next-link {
  padding-right: 10px;
}

.pagination-next-text {
  margin-right: 10px;
}

[dir="rtl"] .pagination-next-link {
  padding-left: 10px;
}

[dir="rtl"] .pagination-next-text {
  margin-left: 10px;
}

.pagination-prev-link {
  padding-left: 10px;
}

.pagination-prev-text {
  margin-left: 10px;
}

[dir="rtl"] .pagination-prev-link {
  padding-right: 10px;
}

[dir="rtl"] .pagination-prev-text {
  margin-right: 10px;
}

/***** Metadata *****/
.meta-group {
  display: block;
}

.meta-group-opposite {
  float: right;
}

[dir="rtl"] .meta-group-opposite {
  float: left;
}

.meta-group * {
  display: inline;
}

.meta-data {
  color: lighten($text_color, 20%);
  font-size: 13px;
}

.meta-data:not(:last-child)::after {
  content: "\00B7";
  margin: 0 5px;
}

/* User Profiles */
.profile-header {
  padding: 30px 0;
  background-color: darken($background_color, 3%);
}

.profile-header .container {
  display: flex;
  flex-wrap: wrap;
}

@media (min-width: 768px) {
  .profile-header .container {
    flex-wrap: nowrap;
  }
}

.profile-header .profile-info {
  flex-basis: 100%;
  display: flex;
  flex-wrap: wrap;
  min-width: 0;
}

.profile-avatar {
  position: relative;
  line-height: 0;
  align-self: center;
  margin-right: 10px;
}

[dir="rtl"] .profile-avatar {
  margin-left: 10px;
  margin-right: 0;
}

.profile-avatar .user-avatar {
  width: 80px;
  height: 80px;
}

.profile-avatar .icon-agent {
  bottom: 0;
  right: 0;
}

.profile-header .basic-info {
  -moz-hyphens: auto;
  -ms-hyphens: auto;
  -webkit-hyphens: auto;
  word-break: break-word;
  word-wrap: break-word;
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 0;
}

.profile-header .basic-info .name {
  margin: 0;
  line-height: 25px;
}

.profile-header .options {
  display: flex;
  flex-basis: 100%;
  margin-top: 12px;
  align-items: flex-start;
  flex-wrap: wrap;
}

@media (min-width: 768px) {
  .profile-header .options {
    flex-wrap: nowrap;
    flex-basis: auto;
    margin-top: 0;
    margin-left: 10px;
  }
  [dir="rtl"] .profile-header .options {
    margin-left: 0;
    margin-right: 10px;
  }
  .profile-header .options > :not(:last-child) {
    margin-bottom: 0;
    margin-right: 10px;
  }
  [dir="rtl"] .profile-header .options > :not(:last-child) {
    margin-left: 10px;
    margin-right: 0;
  }
}

.user-profile-actions {
  width: 100%;
  margin-bottom: 15px;
}

.profile-header .description {
  -moz-hyphens: auto;
  -ms-hyphens: auto;
  -webkit-hyphens: auto;
  word-break: break-word;
  word-wrap: break-word;
  margin: 15px 0;
  flex-basis: 100%;
}

.profile-stats {
  font-size: 13px;
  display: flex;
  flex-direction: column;
  flex-basis: 100%;
}

.profile-stats .stat {
  display: flex;
  margin-bottom: 10px;
}

.profile-stats .stat-label {
  color: lighten($text_color, 20%);
  flex: 0 0 100px;
  margin-right: 10px;
}

[dir="rtl"] .profile-stats .stat-label {
  margin-left: 10px;
  margin-right: 0;
}

.profile-stats-activity {
  border-top: solid 1px #ddd;
  margin-top: 15px;
}

@media (min-width: 768px) {
  .profile-stats-activity {
    border-top: 0;
    flex-direction: row;
  }
}

@media (min-width: 768px) {
  .profile-stats-activity .stat {
    flex-direction: column;
  }
}

.profile-stats-activity .stat:first-child {
  margin-top: 10px;
}

@media (min-width: 768px) {
  .profile-stats-activity .stat:first-child {
    margin-top: 0;
  }
}

@media (min-width: 768px) {
  .profile-stats-activity .stat:not(:last-child) {
    margin-right: 40px;
  }
  [dir="rtl"] .profile-stats-activity .stat:not(:last-child) {
    margin-left: 40px;
    margin-right: 0;
  }
}

@media (min-width: 768px) {
  .profile-stats-activity .stat-label {
    flex: 0 1 auto;
  }
}

.profile-stats-counters {
  border-bottom: solid 1px #ddd;
}

@media (min-width: 768px) {
  .profile-stats-counters {
    flex: 0 0 200px;
    border-bottom: 0;
    margin-left: 40px;
  }
  [dir="rtl"] .profile-stats-counters {
    margin-left: 0;
    margin-right: 40px;
  }
}

@media (min-width: 1024px) {
  .profile-stats-counters {
    flex: 0 0 270px;
    margin-left: 60px;
  }
  [dir="rtl"] .profile-stats-counters {
    margin-right: 60px;
    margin-left: 0;
  }
}

@media (min-width: 768px) {
  .profile-stats-counters .stat {
    flex-direction: column;
  }
}

@media (min-width: 1024px) {
  .profile-stats-counters .stat {
    flex-direction: row;
  }
}

@media (min-width: 768px) {
  .profile-stats-counters .stat:not(:last-child) {
    margin-bottom: 15px;
  }
}

@media (min-width: 768px) {
  .profile-stats-counters .stat-label {
    flex: 0 1 auto;
  }
}

@media (min-width: 1024px) {
  .profile-stats-counters .stat-label {
    flex: 0 0 100px;
  }
}

.profile-private-badge {
  flex-basis: 100%;
  border: solid 1px $brand_color;
  border-radius: 4px;
  color: $brand_color;
  padding: 5px 20px;
  font-size: 12px;
  text-align: center;
}

.profile-private-badge .profile-private-icon {
  margin-left: 5px;
  line-height: 15px;
}

@media (min-width: 768px) {
  .profile-private-badge {
    flex-basis: auto;
  }
}

.profile-nav {
  background-color: darken($background_color, 5%);
  margin-bottom: 37px;
}

.profile-section {
  width: 100%;
}

@media (min-width: 1024px) {
  .profile-section {
    width: calc(100% - 330px);
  }
}

.profile-section-header {
  display: flex;
  flex-wrap: wrap;
}

.profile-section-title {
  flex-basis: 100%;
  margin-bottom: 0;
}

.profile-section-description {
  flex-basis: 100%;
  padding: 10px 0;
  color: lighten($text_color, 20%);
  font-size: 13px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (min-width: 768px) {
  .profile-section-description {
    flex: 1 0 50%;
    padding-bottom: 0;
  }
}

.profile-section-sorter {
  flex-basis: 100%;
  border-top: solid 1px #eee;
  font-size: 13px;
}

.profile-section-sorter .dropdown-toggle {
  padding: 10px 0;
  width: 100%;
}

.profile-section-sorter .dropdown-toggle::after {
  position: absolute;
  right: 0;
}

[dir="rtl"] .profile-section-sorter .dropdown-toggle::after {
  left: 0;
  right: initial;
}

@media (min-width: 768px) {
  .profile-section-sorter .dropdown-toggle::after {
    position: relative;
  }
}

@media (min-width: 768px) {
  .profile-section-sorter {
    flex: 0 1 auto;
    padding-top: 0;
    border-top: 0;
    margin-left: 20px;
  }
  [dir="rtl"] .profile-section-sorter {
    margin-left: 0;
    margin-right: 20px;
  }
}

.profile-badges-items {
  margin-top: 25px;
}

.profile-badges-item {
  border-top: 1px solid #ddd;
  display: flex;
  flex: 1;
  flex-direction: row;
  justify-content: flex-start;
  padding: 27px 12px;
}

.profile-badges-item > div {
  padding-right: 12px;
  padding-left: 12px;
}

.profile-badges-item-image {
  height: 40px;
  width: 40px;
  margin-right: 12px;
}

.profile-badges-item-image img {
  max-height: 40px;
}

[dir="rtl"] .profile-badges-item-image {
  margin-left: 12px;
  margin-right: 0;
}

.profile-badges-item-title, .profile-badges-item-metadata-title {
  font-size: 15px;
  margin-bottom: 10px;
}

.profile-badges-item-title {
  font-weight: 600;
}

.profile-badges-item-description, .profile-badges-item-metadata-description {
  color: lighten($text_color, 20%);
  font-size: 13px;
  margin: 0;
}

.profile-badges-item-metadata {
  margin-left: auto;
  text-align: right;
}

[dir="rtl"] .profile-badges-item-metadata {
  margin-left: 0;
  margin-right: auto;
  text-align: left;
}

.profile-contribution {
  -moz-hyphens: auto;
  -ms-hyphens: auto;
  -webkit-hyphens: auto;
  word-break: break-word;
  word-wrap: break-word;
  padding: 20px 0;
  position: relative;
}

.profile-contribution-header {
  margin-bottom: 5px;
}

.profile-contribution-title {
  margin: 0 0 5px 0;
  display: inline;
  line-height: 21px;
  font-size: 15px;
  vertical-align: middle;
}

.profile-contribution-body {
  margin: 10px 0;
}

.profile-contribution-list > .profile-contribution {
  border-top: 1px solid #eee;
}

@media (min-width: 768px) {
  .profile-contribution-list > .profile-contribution {
    padding-left: 30px;
  }
  [dir="rtl"] .profile-contribution-list > .profile-contribution {
    padding-right: 30px;
    padding-left: 0;
  }
}

.profile-contribution-list > .profile-contribution:last-child {
  border-bottom: 1px solid #eee;
}

.profile-contribution-icon {
  left: 0;
  position: absolute;
  color: #ccc;
  line-height: 25px;
}

[dir="rtl"] .profile-contribution-icon {
  right: 0;
}

.profile-contribution-icon svg {
  vertical-align: middle;
}

.profile-contribution-list .profile-contribution-header {
  margin-left: 30px;
}

[dir="rtl"] .profile-contribution-list .profile-contribution-header {
  padding-right: 30px;
  padding-left: 0;
}

@media (min-width: 768px) {
  .profile-contribution-list .profile-contribution-header {
    margin-left: 0;
  }
  [dir="rtl"] .profile-contribution-list .profile-contribution-header {
    padding-right: 0;
  }
}

.profile-comments .profile-contribution-breadcrumbs {
  margin-left: 30px;
}

[dir="rtl"] .profile-comments .profile-contribution-breadcrumbs {
  padding-right: 30px;
  padding-left: 0;
}

@media (min-width: 768px) {
  .profile-comments .profile-contribution-breadcrumbs {
    margin-left: 0;
  }
  [dir="rtl"] .profile-comments .profile-contribution-breadcrumbs {
    padding-right: 0;
  }
}

.profile-section .no-activity,
.profile-section .private-activity {
  display: block;
  margin-top: 40px;
  color: #999;
}

.private-activity-icon {
  margin-right: 10px;
}

[dir="rtl"] .private-activity-icon {
  margin-right: 0;
  margin-left: 10px;
}

.profile-activity-list {
  margin-top: 25px;
}

.profile-activity {
  position: relative;
  padding-bottom: 30px;
}

@media (min-width: 768px) {
  .profile-activity {
    padding-left: 20px;
  }
  [dir="rtl"] .profile-activity {
    padding-right: 20px;
    padding-left: 0;
  }
}

@media (min-width: 768px) {
  .profile-activity:not(:last-child) {
    border-left: 1px solid #ddd;
  }
  [dir="rtl"] .profile-activity:not(:last-child) {
    border-left: 0;
    border-right: 1px solid #ddd;
  }
}

.profile-activity-header {
  display: flex;
  align-items: center;
  margin-left: 35px;
}

[dir="rtl"] .profile-activity-header {
  margin-left: 0;
  margin-right: 35px;
}

@media (min-width: 768px) {
  .profile-activity-header {
    margin-left: 0;
  }
  [dir="rtl"] .profile-activity-header {
    margin-right: 0;
  }
}

.profile-activity-header .user-avatar {
  width: 40px;
  height: 40px;
  margin-right: 10px;
  min-width: 40px;
  align-self: flex-start;
}

[dir="rtl"] .profile-activity-header .user-avatar {
  margin-left: 10px;
  margin-right: 0;
}

.profile-activity-description {
  -moz-hyphens: auto;
  -ms-hyphens: auto;
  -webkit-hyphens: auto;
  word-break: break-word;
  word-wrap: break-word;
  margin: 0;
  min-width: 0;
  width: 100%;
}

.profile-activity-description span:first-child {
  font-weight: 600;
  display: inline;
}

.profile-activity-contribution {
  padding: 20px;
  margin-top: 10px;
  border-radius: 8px;
  background-color: darken($background_color, 3%);
}

@media (min-width: 768px) {
  .profile-activity-contribution {
    margin-top: 0;
    margin-left: 50px;
  }
  [dir="rtl"] .profile-activity-contribution {
    margin-left: 0;
    margin-right: 50px;
  }
}

.profile-activity-icon {
  position: absolute;
  left: 0;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background-size: 14px 14px;
  background-repeat: no-repeat;
  background-color: $background_color;
  background-position: 50% 50%;
  text-align: center;
  color: #ccc;
}

[dir="rtl"] .profile-activity-icon {
  right: 0;
}

@media (min-width: 768px) {
  .profile-activity-icon {
    left: -14px;
  }
  [dir="rtl"] .profile-activity-icon {
    right: -14px;
  }
}

.profile-activity-icon svg {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  width: 1em;
  height: 1em;
  margin: auto;
}

/***** Search results *****/
.search-results {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
}

@media (min-width: 1024px) {
  .search-results {
    flex-direction: row;
  }
}

.search-results-column {
  flex: 1;
}

@media (min-width: 1024px) {
  .search-results-column {
    flex: 0 0 75%;
  }
}

.search-results-sidebar {
  border-top: 1px solid #ddd;
  flex: 1 0 auto;
  margin-bottom: 20px;
  padding: 0;
}

@media (min-width: 1024px) {
  .search-results-sidebar {
    border: 0;
    flex: 0 0 20%;
    height: auto;
  }
}

.search-results-sidebar .sidenav-item {
  border-radius: 4px;
  padding: 10px 36px;
  margin-bottom: 4px;
  color: $text_color;
}

.search-results-sidebar .sidenav-item:hover, .search-results-sidebar .sidenav-item.current {
  background-color: #e9ebed;
  text-decoration: none;
}

.search-results-sidebar .sidenav-subitem {
  unicode-bidi: embed;
}

.search-results-sidebar .collapsible-sidebar {
  margin-bottom: 30px;
}

.search-results-sidebar .collapsible-sidebar[aria-expanded="false"] .multibrand-filter-list {
  display: none;
}

@media (min-width: 1024px) {
  .search-results-sidebar .collapsible-sidebar[aria-expanded="false"] .multibrand-filter-list {
    display: block;
  }
}

.search-results-sidebar .multibrand-filter-list--collapsed li:nth-child(1n + 6) {
  display: none;
}

.search-results-sidebar .multibrand-filter-list .doc-count {
  color: #666;
}

.search-results-sidebar .see-all-filters {
  background: none;
  border: none;
  cursor: pointer;
  display: block;
  padding: 10px;
  color: $link_color;
}

.search-results-sidebar .see-all-filters[aria-hidden="true"] {
  display: none;
}

.search-results-sidebar .see-all-filters:hover {
  text-decoration: underline;
}

.search-results-sidebar .see-all-filters::after {
  content: ' \2304';
  font-weight: bold;
}

.search-results-subheading {
  font-size: 18px;
  font-weight: 600;
}

.search-results-list {
  margin-bottom: 25px;
}

.search-results-list > li {
  padding: 20px 0;
}

.search-results-list > li:first-child {
  border-top: 1px solid #ddd;
}

.search-results-list > li h2 {
  margin-bottom: 0;
}

.search-results .meta-group {
  display: block;
  align-items: center;
  clear: both;
  color: #666;
}

@media (min-width: 1024px) {
  .search-results .meta-group {
    display: flex;
  }
}

.search-results .meta-group > li {
  display: block;
}

@media (min-width: 1024px) {
  .search-results .meta-group > li {
    display: inline;
  }
}

@media (min-width: 1024px) {
  .search-results .meta-group li:first-child {
    flex: 1;
  }
}

.search-results .meta-group .meta-data {
  color: inherit;
}

[dir="ltr"] .search-results .meta-group .meta-data:not(:last-child) {
  margin-right: 20px;
}

[dir="rtl"] .search-results .meta-group .meta-data:not(:last-child) {
  margin-left: 20px;
}

.search-results .meta-group .meta-data::after {
  content: none;
}

.search-results-description {
  margin-top: 10px;
  word-break: break-word;
}

.search-result-title {
  font-size: 16px;
  display: inline-block;
}

[dir="ltr"] .search-result-icons {
  float: right;
}

[dir="rtl"] .search-result-icons {
  float: left;
}

.search-result-votes, .search-result-meta-count {
  color: lighten($text_color, 20%);
  display: inline-block;
  font-size: 13px;
  padding: 4px 5px;
  position: relative;
}

.search-result-votes-icon, .search-result-meta-count-icon {
  color: $brand_color;
  vertical-align: middle;
  width: 13px;
  height: 13px;
}

[dir="ltr"] .search-result-votes, [dir="ltr"] .search-result-meta-count {
  margin-left: 5px;
}

[dir="ltr"] .search-result-votes::before, [dir="ltr"] .search-result-meta-count::before {
  margin-right: 3px;
}

[dir="rtl"] .search-result-votes, [dir="rtl"] .search-result-meta-count {
  margin-right: 5px;
}

[dir="rtl"] .search-result-votes::before, [dir="rtl"] .search-result-meta-count::before {
  margin-left: 3px;
}

.search-result .meta-group {
  align-items: center;
}

.search-result-breadcrumbs {
  margin: 0;
}

@media (min-width: 1024px) {
  .search-result-breadcrumbs {
    display: table-row;
  }
}

@media (min-width: 1024px) {
  .search-result-breadcrumbs li {
    display: table-cell;
  }
}

/* By default use bold instead of italic to highlight */
.search-results-description em {
  font-style: normal;
  font-weight: bold;
}

/* Add a yellow background for Chinese */
html[lang|="zh"] .search-results-description em {
  font-style: normal;
  background: yellow;
}

/***** Notifications *****/
.notification {
  border: 1px solid;
  display: table;
  font-family: sans-serif;
  font-size: 12px;
  padding: 13px 15px;
  transition: height .2s;
  width: 100%;
  color: #555;
}

.notification a {
  color: #158ec2;
}

.notification-inner {
  margin: 0 auto;
  padding: 0 20px;
  max-width: 980px;
}

.notification-icon, .notification-text, .notification-dismiss {
  display: table-cell;
  vertical-align: middle;
}

.notification-text {
  padding: 0 15px;
  width: 100%;
}

.notification + .notification {
  margin-bottom: -1px;
  position: relative;
  top: -1px;
}

/* Error */
.notification-error {
  background: #ffeded;
  border-color: #f7cbcb;
}

.notification-error .notification-icon::before, .notification-error .notification-inline.notification-error::before {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' focusable='false' viewBox='0 0 12 12'%3E%3Cg fill='none' stroke='%23555555'%3E%3Ccircle cx='5.5' cy='6.5' r='5'/%3E%3Cpath stroke-linecap='round' d='M5.5 3.5v3'/%3E%3C/g%3E%3Ccircle cx='5.5' cy='9' r='1' fill='%23555555'/%3E%3C/svg%3E");
}

/* Notice */
.notification-notice {
  background: #dbf3ff;
  border-color: #b5e0f5;
}

.notification-notice .notification-icon::before, .notification-notice .notification-inline.notification-error::before {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' focusable='false' viewBox='0 0 12 12'%3E%3Cg fill='none' stroke='%23555555'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' d='M3.5 6l2 2L9 4.5'/%3E%3Ccircle cx='6' cy='6' r='5.5'/%3E%3C/g%3E%3C/svg%3E");
}

/* Alert / Lock */
.notification-alert {
  color: #ad5e18;
  background: #fff8ed;
  border-color: #fcdba9;
}

.notification-alert .notification-icon::before, .notification-alert .notification-inline.notification-error::before {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' focusable='false' viewBox='0 0 12 12'%3E%3Cpath fill='none' stroke='%23ad5e18' stroke-linecap='round' d='M5.06 1.27l-4.5 8.5c-.18.33.06.73.44.73h9c.38 0 .62-.4.44-.73l-4.5-8.5a.494.494 0 00-.88 0zM5.5 4v2'/%3E%3Ccircle cx='5.5' cy='8' r='.8' fill='%23ad5e18'/%3E%3C/svg%3E");
}

.notification-icon::before, .notification-inline.notification-error::before {
  background-size: cover;
  content: "";
  display: inline-block;
  height: 14px;
  width: 14px;
  vertical-align: middle;
}

/* Dismiss button */
.notification-dismiss, a.notification-dismiss {
  color: #555;
  cursor: pointer;
  opacity: .6;
  transition: opacity 100ms ease;
  text-decoration: none !important;
}

.notification-dismiss:hover {
  opacity: 1;
}

/* Inline notifications */
.notification-inline {
  border-radius: 4px;
  line-height: 14px;
  margin-top: 5px;
  padding: 5px;
  position: relative;
  text-align: left;
  vertical-align: middle;
}

[dir="rtl"] .notification-inline {
  text-align: right;
}

.notification-inline[aria-hidden="true"] {
  display: none;
}

.notification-inline.notification-error::before {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' focusable='false' viewBox='0 0 12 12'%3E%3Cg fill='none' stroke='%23e35b66'%3E%3Ccircle cx='5.5' cy='6.5' r='5'/%3E%3Cpath stroke-linecap='round' d='M5.5 3.5v3'/%3E%3C/g%3E%3Ccircle cx='5.5' cy='9' r='1' fill='%23e35b66'/%3E%3C/svg%3E");
  margin: -2px 5px 0 0;
}

[dir="rtl"] .notification-inline.notification-error::before {
  margin: 0 0 0 5px;
}

.notification-inline.notification-error {
  background-color: #fff0f1;
  border: 1px solid #e35b66;
  color: #cc3340;
}

.notification-inline.notification-large {
  padding: 13px 15px;
  margin-bottom: 25px;
}

.notification-left-aligned {
  text-align: left;
  padding-left: 0;
}

html[dir="rtl"] .notification-left-aligned {
  text-align: right;
  padding-left: auto;
  padding-right: 0;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-toggle {
  cursor: pointer;
  background: none;
  border: 0;
  display: inline-block;
  padding: 0;
  text-align: initial;
  vertical-align: middle;
}

.dropdown-toggle:hover {
  text-decoration: none;
}

.dropdown-toggle > * {
  display: inline-block;
}

.dropdown-menu {
  background: #fff;
  border: 1px solid #d8d8d8;
  border-radius: 3px;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
  display: none;
  font-size: 14px;
  font-style: normal;
  font-weight: normal;
  left: 0;
  margin-top: 1px;
  min-width: 170px;
  padding: 10px 0;
  position: absolute;
  text-align: left;
  z-index: 1000;
}

[dir="rtl"] .dropdown-menu {
  text-align: right;
}

.dropdown-menu[aria-expanded="true"] {
  display: block;
}

.dropdown-menu [role="separator"] {
  border-bottom: 1px solid #e9ebed;
  margin: 4px 0;
}

.dropdown-menu [role="menuitem"] {
  color: #333;
  cursor: pointer;
  display: block;
  padding: 7px 40px 7px 20px;
  white-space: nowrap;
  background-color: transparent;
  border: 0;
  -webkit-appearance: none;
  text-align: start;
  line-height: inherit;
  width: 100%;
}

[dir="rtl"] .dropdown-menu [role="menuitem"] {
  padding: 7px 20px 7px 40px;
}

.dropdown-menu [role="menuitem"]:hover, .dropdown-menu [role="menuitem"]:focus {
  background: #f3f3f3;
  text-decoration: none;
  color: #333;
}

.dropdown-menu [role="menuitem"][aria-selected="true"] {
  cursor: default;
}

.dropdown-menu [role="menuitem"][aria-selected="true"]::after {
  content: "";
  background-image: url("data:image/svg+xml,%3Csvg aria-hidden='true' xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='none' stroke='currentColor' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M1 7l3 3 7-7'%3E%3C/path%3E%3C/svg%3E");
  display: inline-block;
  height: 12px;
  margin-left: 10px;
  width: 12px;
}

[dir="rtl"] .dropdown-menu [role="menuitem"][aria-selected="true"]::after {
  margin-left: 0;
  margin-right: 10px;
  float: left;
}

.dropdown-menu [role="menuitem"][hidden], .dropdown-menu [role="menuitem"][aria-hidden="true"] {
  display: none !important;
}

.dropdown-menu-end {
  left: auto;
  right: 0;
}

.dropdown-menu-top {
  bottom: 100%;
  margin-bottom: 1px;
}

[dir="rtl"] .dropdown-menu {
  left: auto;
  right: 0;
  text-align: right;
}

[dir="rtl"] .dropdown-menu-end {
  left: 0;
  right: auto;
}

.dropdown-chevron-icon {
  vertical-align: middle;
}
/* Alternate b2uttons */
input[type="submit"],
.btn--primary,
.section-subscribe button,
.lt-article-subscribe button,
.lt-community-follow button,
.subscriptions-subscribe button,
.lt-profile__buttons button,
.lt-profile__buttons a {
  color: #fff;
  background-color: #F14B62;
  border-color: #F14B62;
}

input[type="submit"]:hover,
input[type="submit"]:focus,
input[type="submit"]:active,
.btn--primary:hover,
.btn--primary:focus,
.btn--primary:active,
.section-subscribe button:hover,
.section-subscribe button:focus,
.section-subscribe button:active,
.lt-article-subscribe button:hover,
.lt-article-subscribe button:focus,
.lt-article-subscribe button:active,
.lt-community-follow button:hover,
.lt-community-follow button:focus,
.lt-community-follow button:active,
.subscriptions-subscribe button:hover,
.subscriptions-subscribe button:focus,
.subscriptions-subscribe button:active,
.lt-profile__buttons button:hover,
.lt-profile__buttons button:focus,
.lt-profile__buttons button:active,
.lt-profile__buttons a:hover,
.lt-profile__buttons a:focus,
.lt-profile__buttons a:active {
  color: #fff;
  background-color: #ec1231;
  border-color: #ec1231;
}

.btn--topbar {
  color: #2B2B2B;
  background-color: transparent;
  border: var(--border-width) solid #2B2B2B;
  border-radius: 100px;
}

.btn--topbar:hover {
  opacity: 1;
}

.btn--topbar:active {
  box-shadow: none;
}

.btn--topbar:hover,
.btn--topbar:focus,
.btn--topbar:active {
  color: #e0e0e0;
  background-color: transparent;
  border-color: #e0e0e0;
}
@media (min-width: 768px) {
  .btn--topbar {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: top;
  }
}
@media (max-width: 767px) {
  .btn--topbar {
    display: block;
    width: 100%;
    margin-bottom: calc(var(--line-height-computed) / 2);
  }

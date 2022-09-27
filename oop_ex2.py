<div class="container-divider"></div>
<div class="container">
  <nav class="sub-nav">
    {{breadcrumbs}}

  </nav>

  <div class="category-container">
    <div class="category-content">
      <header class="page-header page-header--center">
        <h1>{{category.name}}</h1>
        {{#if category.description}}
          <p class="page-header-description">{{category.description}}</p>
        {{/if}}
      </header>

      <div id="main-content" class="row section-tree clearfix">
        {{#each sections}}
          <section class="column column--sm-6 section">
            <h3 class="section__title-link ">
              <a href="{{url}}">{{name}}</a>
            </h3>
            {{#if articles}}
              <ul class="article-list ">
                {{#each articles}}
                  <li class="article-list-item {{#if promoted}} article-promoted{{/if}}">
                    {{#if promoted}}
                      <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" focusable="false" viewBox="0 0 12 12" class="icon-star" title="{{t 'promoted'}}">
                        <path fill="currentColor" d="M2.88 11.73c-.19 0-.39-.06-.55-.18a.938.938 0 01-.37-1.01l.8-3L.35 5.57a.938.938 0 01-.3-1.03c.12-.37.45-.63.85-.65L4 3.73 5.12.83c.14-.37.49-.61.88-.61s.74.24.88.6L8 3.73l3.11.17a.946.946 0 01.55 1.68L9.24 7.53l.8 3a.95.95 0 01-1.43 1.04L6 9.88l-2.61 1.69c-.16.1-.34.16-.51.16z"/>
                      </svg>
                    {{/if}}

                    <a href="{{url}}" class="article-list-link">{{title}}</a>
                    {{#if internal}}
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" focusable="false" viewBox="0 0 16 16" class="icon-lock" title="{{t 'internal'}}">
                        <rect width="12" height="9" x="2" y="7" fill="currentColor" rx="1" ry="1"/>
                        <path fill="none" stroke="currentColor" d="M4.5 7.5V4a3.5 3.5 0 017 0v3.5"/>
                      </svg>
                    {{/if}}
                  </li>
                {{/each}}
              </ul>
              {{#if more_articles}}
                <a href="{{url}}" class="btn btn--primary see-all-articles">
                  {{t 'show_all_articles' count=article_count}}
                </a>
              {{/if}}
            {{/if}}
          </section>
          <section class="column column--sm-6 section">
            <h3 class="section__title-link ">
              <a href="{{url}}">{{name}}</a>
            </h3>
            {{#if articles}}
              <ul class="article-list ">
                {{#each articles}}
                  <li class="article-list-item {{#if promoted}} article-promoted{{/if}}">
        {{else}}
          <i class="category-empty">
            <a href="{{category.url}}">{{t 'empty'}}</a>
          </i>
        {{/each}}
      </div>
    </div>
  </div>
</div>

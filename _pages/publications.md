---
layout: page
permalink: /publications/
title: publications
description: Please see [Google Scholar](https://scholar.google.com/citations?user=6hu7hXkAAAAJ&hl=en) for more recent works and arXiv papers. 
years: [2024,2023]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

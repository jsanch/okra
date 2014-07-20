




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>okra/app.py at master · sudov/okra</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="sudov/okra" name="twitter:title" /><meta content="okra - Split" name="twitter:description" /><meta content="https://avatars3.githubusercontent.com/u/4527576?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars3.githubusercontent.com/u/4527576?s=400" property="og:image" /><meta content="sudov/okra" property="og:title" /><meta content="https://github.com/sudov/okra" property="og:url" /><meta content="okra - Split" property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets" />

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="D106017C:22D4:87C217:53CB261C" name="octolytics-dimension-request_id" /><meta content="4527576" name="octolytics-actor-id" /><meta content="sudov" name="octolytics-actor-login" /><meta content="3dd4edd8f55420228719812e729c5f00682a12d9a3df17239a15971421f28a3e" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="6906olaAYw8Jw2mNrZZsf/ayxHE/+bkoBez7RrGgcAM7hl9gq4fl8Ut23zNefH77eLdfPO2kcKByBN7KV8mCqA==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-08cc4d21dbfdd953c85afbf75762f5b6e145620d.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-7fa45bc1a10ba6acbc768b848364578bfb855eac.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="db52f4e25078b55191f8b1f2d9a3a573">

      
  <meta name="description" content="okra - Split" />


  <meta content="4527576" name="octolytics-dimension-user_id" /><meta content="sudov" name="octolytics-dimension-user_login" /><meta content="21995521" name="octolytics-dimension-repository_id" /><meta content="sudov/okra" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="21995521" name="octolytics-dimension-repository_network_root_id" /><meta content="sudov/okra" name="octolytics-dimension-repository_network_root_nwo" />

  <link href="https://github.com/sudov/okra/commits/master.atom" rel="alternate" title="Recent Commits to okra:master" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production macintosh vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


    
    <a href="/notifications" aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s" data-hotkey="g n">
        <span class="mail-status all-read"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="sudov"
    data-repo="sudov/okra"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="sudov/okra" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    

<ul id="user-links">
  <li>
    <a href="/sudov" class="name">
      <img alt="sudov" class=" js-avatar" data-user="4527576" height="20" src="https://avatars0.githubusercontent.com/u/4527576?s=140" width="20" /> sudov
    </a>
  </li>

  <li class="new-menu dropdown-toggle js-menu-container">
    <a href="#" class="js-menu-target tooltipped tooltipped-s" aria-label="Create new...">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-arrow"></span>
    </a>

    <div class="new-menu-content js-menu-content">
    </div>
  </li>

  <li>
    <a href="/settings/profile" id="account_settings"
      class="tooltipped tooltipped-s"
      aria-label="Account settings ">
      <span class="octicon octicon-tools"></span>
    </a>
  </li>
  <li>
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="stdMB8nzXsqFwyBL1WAr5fP4Dck20I933J+t2e28MmQzrSY/1G1vALUQ1s3yDyObHWbpFosp/5Y7MGKPWdbE4g==" /></div>
      <button class="sign-out-button tooltipped tooltipped-s" aria-label="Sign out">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="section-title">
      <span title="sudov/okra">This repository</span>
    </li>
      <li>
        <a href="/sudov/okra/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
      <li>
        <a href="/sudov/okra/settings/collaboration"><span class="octicon octicon-person"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

        



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="GwMQxF+7XdKNw94zQ80/g+jT9GJjcjTaOUlpe/VMTwhAwB09DkTw/TRVvVpXm+iK+NAyLhwIIVIq/DFFAJSj3A==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="21995521" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/sudov/okra/watchers">
        5
      </a>
      <a href="/sudov/okra/subscription"
        class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye"></span>
          Unwatch
        </span>
      </a>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
            <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">Be notified when participating or @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">Be notified of all conversations.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">Never be notified.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
    

  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/sudov/okra/unstar" class="js-toggler-form starred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="nnHEQaNWNgdhfDgLluXK6hR9LqN/043Xfo5AeGovKhsGxbYTw8Fe0FHrAj7dpSkbcv+mR+sKWMpfAGh8tGaHrw==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Unstar this repository" title="Unstar sudov/okra">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/sudov/okra/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/sudov/okra/star" class="js-toggler-form unstarred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="oKJ8YCJOoPtL96T3k+eVuUk2Zi5VuVY1zLdgKM+6CGVCjiu7fmyK3yUrjOpn6+RH5MRxuMk5ulxDFtOHZ8I/Hg==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Star this repository" title="Star sudov/okra">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/sudov/okra/stargazers">
          0
        </a>
</form>  </div>

  </li>


        <li>
          <a href="/sudov/okra/fork" class="minibutton with-count js-toggler-target fork-button lighter tooltipped-n" title="Fork your own copy of sudov/okra to your account" aria-label="Fork your own copy of sudov/okra to your account" rel="nofollow" data-method="post">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/sudov/okra/network" class="social-count">0</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/sudov" class="url fn" itemprop="url" rel="author"><span itemprop="title">sudov</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/sudov/okra" class="js-current-repository js-repo-home-link">okra</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/sudov/okra" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /sudov/okra">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/sudov/okra/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /sudov/okra/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/sudov/okra/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /sudov/okra/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped tooltipped-w" aria-label="Wiki">
          <a href="/sudov/okra/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g w" data-selected-links="repo_wiki /sudov/okra/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/sudov/okra/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /sudov/okra/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/sudov/okra/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /sudov/okra/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/sudov/okra/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /sudov/okra/network">
          <span class="octicon octicon-repo-forked"></span> <span class="full-word">Network</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


      <div class="sunken-menu-separator"></div>
      <ul class="sunken-menu-group">
        <li class="tooltipped tooltipped-w" aria-label="Settings">
          <a href="/sudov/okra/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_settings /sudov/okra/settings">
            <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
      </ul>
  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/sudov/okra.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/sudov/okra.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:sudov/okra.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="git@github.com:sudov/okra.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/sudov/okra" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/sudov/okra" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>

  <a href="http://mac.github.com" data-url="github-mac://openRepo/https://github.com/sudov/okra" class="minibutton sidebar-button js-conduit-rewrite-url" title="Save sudov/okra to your computer and use it in GitHub Desktop." aria-label="Save sudov/okra to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/sudov/okra/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download sudov/okra as a zip file"
                   title="Download sudov/okra as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/sudov/okra/blob/aeced678d069e29144eab4996b79e8c2c77c758c/app.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:b07f190210f284b0049bce91b559e3df -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sudov/okra/blob/dan/app.py"
                 data-name="dan"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="dan">dan</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/sudov/okra/blob/master/app.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/sudov/okra/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="4dI8ERipxkn2vDn6LVrjSJOjSBTs5vLBAdcVf2TWCtAlOpgcnDv0kskjVhyzb1tY4gD9zJIPI+fQINnB3wlshA==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master" />
            <input type="hidden" name="path" id="path" value="app.py" />
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/sudov/okra/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="app.py"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/sudov/okra" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">okra</span></a></span></span><span class="separator"> / </span><strong class="final-path">app.py</strong>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/sudov/okra/contributors/master/app.py">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>382 lines (296 sloc)</span>
          <span class="meta-divider"></span>
        <span>12.103 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
            <a class="minibutton tooltipped tooltipped-w js-conduit-openfile-check"
               href="http://mac.github.com"
               data-url="github-mac://openRepo/https://github.com/sudov/okra?branch=master&amp;filepath=app.py"
               aria-label="Open this file in GitHub for Mac"
               data-failed-title="Your version of GitHub for Mac is too old to open this file. Try checking for updates.">
                <span class="octicon octicon-device-desktop"></span> Open
            </a>
                <a class="minibutton js-update-url-with-hash"
                   href="/sudov/okra/edit/master/app.py"
                   data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
          <a href="/sudov/okra/raw/master/app.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/sudov/okra/blame/master/app.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/sudov/okra/commits/master/app.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

            <a class="minibutton danger empty-icon"
               href="/sudov/okra/delete/master/app.py"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">

          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python js-blob-data">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC2'><span class="kn">from</span> <span class="nn">flask</span> <span class="kn">import</span> <span class="n">Flask</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">redirect</span><span class="p">,</span> <span class="n">render_template</span><span class="p">,</span> <span class="n">url_for</span><span class="p">,</span> <span class="n">jsonify</span><span class="p">,</span> <span class="n">send_from_directory</span><span class="p">,</span> <span class="n">session</span></div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">werkzeug.utils</span> <span class="kn">import</span> <span class="n">secure_filename</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">pymongo</span> <span class="kn">import</span> <span class="n">MongoClient</span></div><div class='line' id='LC5'><span class="kn">from</span> <span class="nn">threading</span> <span class="kn">import</span> <span class="n">Thread</span></div><div class='line' id='LC6'><span class="kn">import</span> <span class="nn">json</span></div><div class='line' id='LC7'><span class="kn">from</span> <span class="nn">bson</span> <span class="kn">import</span> <span class="n">Binary</span><span class="p">,</span> <span class="n">Code</span></div><div class='line' id='LC8'><span class="kn">from</span> <span class="nn">bson.json_util</span> <span class="kn">import</span> <span class="n">dumps</span></div><div class='line' id='LC9'><span class="kn">from</span> <span class="nn">charge</span> <span class="kn">import</span> <span class="o">*</span></div><div class='line' id='LC10'><span class="kn">from</span> <span class="nn">constants</span> <span class="kn">import</span> <span class="n">CONSUMER_ID</span><span class="p">,</span> <span class="n">CONSUMER_SECRET</span><span class="p">,</span> <span class="n">APP_SECRET</span></div><div class='line' id='LC11'><span class="kn">import</span> <span class="nn">requests</span></div><div class='line' id='LC12'><span class="kn">import</span> <span class="nn">scan.okraparser</span></div><div class='line' id='LC13'><span class="c"># import scan.okraparser.OkraParseException</span></div><div class='line' id='LC14'><br/></div><div class='line' id='LC15'><span class="n">app</span> <span class="o">=</span> <span class="n">Flask</span><span class="p">(</span><span class="n">__name__</span><span class="p">)</span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><span class="n">app</span><span class="o">.</span><span class="n">secret_key</span> <span class="o">=</span> <span class="n">APP_SECRET</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'><span class="c">################################ DB ####################################</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="k">def</span> <span class="nf">get_db_conection</span><span class="p">(</span><span class="n">db</span><span class="p">):</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">client</span> <span class="o">=</span> <span class="n">MongoClient</span><span class="p">()</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">client</span><span class="p">[</span><span class="n">db</span><span class="p">]</span></div><div class='line' id='LC29'><span class="k">def</span> <span class="nf">get_db_collection</span><span class="p">(</span><span class="n">collection</span><span class="p">):</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">get_db_conection</span><span class="p">(</span><span class="s">&#39;okra&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">okra</span><span class="p">[</span><span class="n">collection</span><span class="p">]</span></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'><span class="c">########################################################################</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'><span class="c">#############################   TAB      #########################</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><span class="c"># CREATE TAB</span></div><div class='line' id='LC38'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/create_tab&#39;</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;POST&#39;</span><span class="p">,</span> <span class="s">&#39;GET&#39;</span><span class="p">])</span></div><div class='line' id='LC39'><span class="k">def</span> <span class="nf">create_tab</span><span class="p">():</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span> <span class="o">=</span> <span class="n">get_db_conection</span><span class="p">(</span><span class="s">&quot;okra&quot;</span><span class="p">)</span> <span class="c">#get conncection</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># tabs = db.tabs #get tabs collection</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;tabs&#39;</span><span class="p">)</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># invites = db.invites #get invites collection</span></div><div class='line' id='LC44'><br/></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s">&#39;POST&#39;</span><span class="p">:</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#MUST VALIDATE</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_group</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;group&#39;</span><span class="p">]</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_items</span> <span class="o">=</span> <span class="n">dumps</span><span class="p">(</span><span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;items&#39;</span><span class="p">])</span> <span class="c">#convert to json</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_subtotal</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;subtotal&#39;</span><span class="p">]</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_total</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;total&#39;</span><span class="p">]</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_tip</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;tip&#39;</span><span class="p">]</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_tax</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;tax&#39;</span><span class="p">]</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#prepare for db entry</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;id&#39;</span> <span class="p">:</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">],</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;title&#39;</span> <span class="p">:</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;title&#39;</span><span class="p">],</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;group&#39;</span> <span class="p">:</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;group&#39;</span><span class="p">],</span> <span class="c">#array of user ids</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;items&#39;</span> <span class="p">:</span> <span class="n">tab_items</span><span class="p">,</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;subtotal&#39;</span> <span class="p">:</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;subtotal&#39;</span><span class="p">],</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;total&#39;</span> <span class="p">:</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;total&#39;</span><span class="p">],</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;tip&#39;</span> <span class="p">:</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;tip&#39;</span><span class="p">],</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;tax&#39;</span> <span class="p">:</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;tax&#39;</span><span class="p">]</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs_id</span> <span class="o">=</span> <span class="n">tabs</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">tab</span><span class="p">)</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'><br/></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># create invites from group.</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">create_invites</span><span class="p">(</span><span class="n">tab_group</span><span class="p">,</span> <span class="n">tab_id</span><span class="p">)</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;items = &#39;</span> <span class="o">+</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="n">tabs_id</span><span class="p">})[</span><span class="s">&#39;items&#39;</span><span class="p">]</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;inserted tab with tab_id: &#39;</span> <span class="o">+</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;_id&quot;</span><span class="p">:</span><span class="n">tabs_id</span><span class="p">})[</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;not a post request&quot;</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'><span class="c"># GET TAB</span></div><div class='line' id='LC80'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/get_tab&#39;</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;GET&#39;</span><span class="p">])</span></div><div class='line' id='LC81'><span class="k">def</span> <span class="nf">get_tab</span><span class="p">():</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Returns tab object in json for requested tab_id&#39;&#39;&#39;</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span> <span class="o">=</span> <span class="n">get_db_conection</span><span class="p">(</span><span class="s">&quot;okra&quot;</span><span class="p">)</span> <span class="c">#get conncection</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">tabs</span> <span class="c">#get tabs collection</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;tab_id&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC86'><br/></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span> <span class="o">=</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span> <span class="p">:</span> <span class="n">tab_id</span><span class="p">})</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">json1</span> <span class="o">=</span> <span class="n">dumps</span><span class="p">(</span><span class="n">le_tab</span><span class="p">)</span></div><div class='line' id='LC89'><br/></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">json1</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'><span class="c"># UPDATE TAB ITEMS</span></div><div class='line' id='LC93'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/update_tab_items&#39;</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;POST&#39;</span><span class="p">])</span></div><div class='line' id='LC94'><span class="k">def</span> <span class="nf">update_tab_items</span><span class="p">():</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39; updates items in a tab &#39;&#39;&#39;</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;tabs&#39;</span><span class="p">)</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;tab_id&#39;</span><span class="p">]</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span> <span class="o">=</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span> <span class="p">:</span> <span class="n">tab_id</span><span class="p">})</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">le_tab</span> <span class="o">==</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;Tab not found&#39;</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span>   <span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;items&#39;</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;jello&#39;</span></div><div class='line' id='LC104'><br/></div><div class='line' id='LC105'><span class="c"># UPDATE TAB BILL</span></div><div class='line' id='LC106'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/update_tab_bill&#39;</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;POST&#39;</span><span class="p">])</span></div><div class='line' id='LC107'><span class="k">def</span> <span class="nf">update_tab_bill</span><span class="p">(</span><span class="n">bill_json</span><span class="p">):</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Updates tab to add each bill items description and value&#39;&#39;&#39;</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span> <span class="o">=</span> <span class="n">get_db_conection</span><span class="p">(</span><span class="s">&quot;okra&quot;</span><span class="p">)</span>   <span class="c">#get conncection</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;tabs&#39;</span><span class="p">)</span><span class="c">#get tabs collection</span></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;tab_id&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span> <span class="o">=</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span> <span class="p">:</span> <span class="n">tab_id</span><span class="p">})</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#whatever stevens json collection is called</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bill_json</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;bill_json&#39;</span><span class="p">)</span></div><div class='line' id='LC117'><br/></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#Insert bill items to tab</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;items_prices&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">bill_json</span><span class="p">[</span><span class="s">&#39;tab_items&#39;</span><span class="p">]</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;total&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">bill_json</span><span class="p">[</span><span class="s">&#39;tab_meta&#39;</span><span class="p">]</span></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">le_tab</span><span class="p">)</span></div><div class='line' id='LC123'><br/></div><div class='line' id='LC124'><br/></div><div class='line' id='LC125'><span class="c">########################################################################</span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'><br/></div><div class='line' id='LC128'><br/></div><div class='line' id='LC129'><span class="c">############################## USERS   ###########################</span></div><div class='line' id='LC130'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/add_user&#39;</span> <span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;POST&#39;</span><span class="p">,</span> <span class="s">&#39;GET&#39;</span><span class="p">])</span></div><div class='line' id='LC131'><span class="k">def</span> <span class="nf">add_user</span><span class="p">():</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">users</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;users&#39;</span><span class="p">)</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">request</span><span class="o">.</span><span class="n">method</span> <span class="o">==</span> <span class="s">&#39;POST&#39;</span><span class="p">:</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_phone</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;phone&#39;</span><span class="p">]</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_name</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;name&#39;</span><span class="p">]</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_friends</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;friends&#39;</span><span class="p">]</span> <span class="c">#list</span></div><div class='line' id='LC138'><br/></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;id&#39;</span> <span class="p">:</span> <span class="n">user_id</span><span class="p">,</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;phone&#39;</span> <span class="p">:</span> <span class="n">user_phone</span><span class="p">,</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;name&#39;</span> <span class="p">:</span> <span class="n">user_name</span><span class="p">,</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;friends&#39;</span> <span class="p">:</span> <span class="n">user_friends</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">users</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">user</span><span class="p">)</span></div><div class='line' id='LC146'><br/></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;registerd user: &quot;</span> <span class="o">+</span> <span class="n">users</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span><span class="p">:</span><span class="n">user_id</span><span class="p">})[</span><span class="s">&#39;id&#39;</span><span class="p">]</span></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'><span class="c">#GET USER</span></div><div class='line' id='LC150'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/get_user&#39;</span><span class="p">)</span></div><div class='line' id='LC151'><span class="k">def</span> <span class="nf">get_user</span><span class="p">():</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39; gets a user_id and returns json info of user &#39;&#39;&#39;</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">users</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;users&#39;</span><span class="p">)</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;user_id&#39;</span><span class="p">)</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">json</span> <span class="o">=</span> <span class="n">dumps</span><span class="p">(</span><span class="n">users</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span><span class="p">:</span><span class="n">user_id</span><span class="p">}))</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;hello&#39;</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span>  <span class="n">json</span></div><div class='line' id='LC158'><br/></div><div class='line' id='LC159'><span class="c">#GET FRIENDS</span></div><div class='line' id='LC160'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/get_friends&#39;</span><span class="p">)</span></div><div class='line' id='LC161'><span class="k">def</span> <span class="nf">get_friends</span><span class="p">():</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39; gets the list of friends with their ids and names for a given user id &#39;&#39;&#39;</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">users</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;users&#39;</span><span class="p">)</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;user_id&#39;</span><span class="p">)</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="n">users</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&#39;id&#39;</span><span class="p">:</span><span class="n">user_id</span><span class="p">})</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">friend_ids</span> <span class="o">=</span> <span class="n">user</span><span class="p">[</span><span class="s">&#39;friends&#39;</span><span class="p">]</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">friends</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">friend_id</span> <span class="ow">in</span> <span class="n">friend_ids</span><span class="p">:</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="n">users</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&#39;id&#39;</span><span class="p">:</span><span class="n">friend_id</span><span class="p">})[</span><span class="s">&#39;name&#39;</span><span class="p">]</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">friends</span><span class="p">[</span><span class="n">friend_id</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">name</span><span class="p">:</span><span class="s">&#39;name&#39;</span><span class="p">}</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">friends</span></div><div class='line' id='LC172'><br/></div><div class='line' id='LC173'><span class="c">########################################################################</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'><span class="c">##############################    ITEMS   #############################</span></div><div class='line' id='LC176'><span class="c">#ASSIGN ITEM</span></div><div class='line' id='LC177'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/assign_item&#39;</span><span class="p">)</span></div><div class='line' id='LC178'><span class="k">def</span> <span class="nf">assign_item</span><span class="p">(</span><span class="n">tab_id</span><span class="p">,</span> <span class="n">item_id</span><span class="p">,</span> <span class="n">user_id</span><span class="p">):</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39; gets the list of friends with their ids and names for a given user id &#39;&#39;&#39;</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;tabs&#39;</span><span class="p">)</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;tab_id&#39;</span><span class="p">]</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span> <span class="o">=</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span> <span class="p">:</span> <span class="n">tab_id</span><span class="p">})</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;items&#39;</span><span class="p">][</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">le_tab</span><span class="p">)</span></div><div class='line' id='LC186'><br/></div><div class='line' id='LC187'><span class="c">#UNASSIGN ITEM</span></div><div class='line' id='LC188'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/unassign_item&#39;</span><span class="p">)</span></div><div class='line' id='LC189'><span class="k">def</span> <span class="nf">unassign_item</span><span class="p">(</span><span class="n">tab_id</span><span class="p">,</span> <span class="n">item_id</span><span class="p">,</span> <span class="n">user_id</span><span class="p">):</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39; gets the list of friends with their ids and names for a given user id &#39;&#39;&#39;</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;tabs&#39;</span><span class="p">)</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">form</span><span class="p">[</span><span class="s">&#39;tab_id&#39;</span><span class="p">]</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span> <span class="o">=</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span> <span class="p">:</span> <span class="n">tab_id</span><span class="p">})</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;items&#39;</span><span class="p">][</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">number_of_users</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;items&#39;</span><span class="p">][</span><span class="mi">2</span><span class="p">])</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">remove_location</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">i</span><span class="o">=</span><span class="mi">0</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">number_of_users</span><span class="p">):</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;items&#39;</span><span class="p">][</span><span class="mi">2</span><span class="p">][</span><span class="n">i</span><span class="p">]</span> <span class="o">==</span> <span class="n">user_id</span><span class="p">):</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">remove_location</span> <span class="o">=</span> <span class="n">i</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">remove_location</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">):</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;items&#39;</span><span class="p">][</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">remove_location</span><span class="p">)</span>      </div><div class='line' id='LC205'><br/></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">le_tab</span><span class="p">)</span>    </div><div class='line' id='LC207'><br/></div><div class='line' id='LC208'><span class="c">############################## INVITE shit  ############################</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'><span class="k">def</span> <span class="nf">create_invites</span><span class="p">(</span><span class="n">group</span><span class="p">,</span> <span class="n">tab_id</span><span class="p">):</span> <span class="c">#used by create tab to invite users that are added.</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">invites</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;invites&#39;</span><span class="p">)</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Creating invites for &quot;</span> <span class="o">+</span>  <span class="n">group</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">users</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="n">group</span><span class="p">)</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">user_id</span> <span class="ow">in</span> <span class="n">users</span><span class="p">:</span></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="nb">str</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span> <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="n">tab_id</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">invite</span> <span class="o">=</span> <span class="p">{</span> <span class="s">&#39;user_id&#39;</span><span class="p">:</span> <span class="n">user_id</span><span class="p">,</span> <span class="s">&#39;tab_id&#39;</span> <span class="p">:</span> <span class="n">tab_id</span> <span class="p">}</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">invite_id</span> <span class="o">=</span> <span class="n">invites</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">invite</span><span class="p">)</span></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'><span class="c">#poll invite</span></div><div class='line' id='LC220'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/poll_for_invite&#39;</span><span class="p">)</span></div><div class='line' id='LC221'><span class="k">def</span> <span class="nf">poll_for_invite</span><span class="p">():</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Returns tab_id if the passed user_id has an invite &#39;&#39;&#39;</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#get db collection</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">invites</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;invites&#39;</span><span class="p">)</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#get param</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req_user_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;user_id&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;requested user id : &quot;</span> <span class="o">+</span>  <span class="n">req_user_id</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">inv</span> <span class="o">=</span> <span class="n">invites</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&#39;user_id&#39;</span><span class="p">:</span><span class="n">req_user_id</span><span class="p">})</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">inv</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span> <span class="n">inv</span> <span class="o">==</span> <span class="bp">None</span> <span class="p">):</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;null&#39;</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">inv</span><span class="p">[</span><span class="s">&#39;tab_id&#39;</span><span class="p">]</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'><br/></div><div class='line' id='LC236'><br/></div><div class='line' id='LC237'><span class="c">########################################################################</span></div><div class='line' id='LC238'><br/></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'><br/></div><div class='line' id='LC241'><span class="c">############################# UPLAOD IMAGE #############################</span></div><div class='line' id='LC242'><span class="c"># This is the path to the upload directory</span></div><div class='line' id='LC243'><span class="n">app</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s">&#39;UPLOAD_FOLDER&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;images/&#39;</span></div><div class='line' id='LC244'><span class="c"># These are the extension that we are accepting to be uploaded</span></div><div class='line' id='LC245'><span class="n">app</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s">&#39;ALLOWED_EXTENSIONS&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">([</span><span class="s">&#39;txt&#39;</span><span class="p">,</span> <span class="s">&#39;pdf&#39;</span><span class="p">,</span> <span class="s">&#39;png&#39;</span><span class="p">,</span> <span class="s">&#39;jpg&#39;</span><span class="p">,</span> <span class="s">&#39;jpeg&#39;</span><span class="p">,</span> <span class="s">&#39;gif&#39;</span><span class="p">])</span></div><div class='line' id='LC246'><br/></div><div class='line' id='LC247'><span class="c"># For a given file, return whether it&#39;s an allowed type or not</span></div><div class='line' id='LC248'><span class="k">def</span> <span class="nf">allowed_file</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;.&#39;</span> <span class="ow">in</span> <span class="n">filename</span> <span class="ow">and</span> \</div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span><span class="o">.</span><span class="n">rsplit</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span> <span class="ow">in</span> <span class="n">app</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s">&#39;ALLOWED_EXTENSIONS&#39;</span><span class="p">]</span></div><div class='line' id='LC251'><br/></div><div class='line' id='LC252'><br/></div><div class='line' id='LC253'><span class="c"># This route will show a form to perform an AJAX request</span></div><div class='line' id='LC254'><span class="c"># jQuery is loaded to execute the request and update the</span></div><div class='line' id='LC255'><span class="c"># value of the operation</span></div><div class='line' id='LC256'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/img-upload&#39;</span><span class="p">)</span></div><div class='line' id='LC257'><span class="k">def</span> <span class="nf">img_upload</span><span class="p">():</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">render_template</span><span class="p">(</span><span class="s">&#39;img-upload.html&#39;</span><span class="p">)</span></div><div class='line' id='LC259'><br/></div><div class='line' id='LC260'><span class="c"># Route that will process the file upload</span></div><div class='line' id='LC261'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/upload&#39;</span><span class="p">,</span> <span class="n">methods</span><span class="o">=</span><span class="p">[</span><span class="s">&#39;POST&#39;</span><span class="p">])</span></div><div class='line' id='LC262'><span class="k">def</span> <span class="nf">upload</span><span class="p">():</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Get the name of the uploaded file</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">files</span><span class="p">[</span><span class="s">&#39;file&#39;</span><span class="p">]</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Check if the file is one of the allowed types/extensions</span></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">file</span> <span class="ow">and</span> <span class="n">allowed_file</span><span class="p">(</span><span class="nb">file</span><span class="o">.</span><span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Make the filename safe, remove unsupported chars</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">secure_filename</span><span class="p">(</span><span class="nb">file</span><span class="o">.</span><span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Move the file form the temporal folder to</span></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the upload folder we setup</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">file</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">app</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s">&#39;UPLOAD_FOLDER&#39;</span><span class="p">],</span> <span class="n">filename</span><span class="p">))</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Redirect the user to the uploaded_file route, which</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># will basicaly show on the browser the uploaded file</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">thr</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span><span class="n">target</span> <span class="o">=</span> <span class="n">async_parse</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="p">[</span><span class="n">filename</span><span class="p">])</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">thr</span><span class="o">.</span><span class="n">start</span><span class="p">()</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;uploaded - async analyzing&#39;</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># return redirect(url_for(&#39;uploaded_file&#39;,</span></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># filename=filename))</span></div><div class='line' id='LC279'><br/></div><div class='line' id='LC280'><span class="k">def</span> <span class="nf">async_parse</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tabs</span> <span class="o">=</span> <span class="n">scan</span><span class="o">.</span><span class="n">okraparser</span><span class="o">.</span><span class="n">full_scan</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">tabs</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span> <span class="o">=</span> <span class="n">get_db_conection</span><span class="p">(</span><span class="s">&quot;okra&quot;</span><span class="p">)</span>   <span class="c">#get conncection</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># tabs = get_db_collection(&#39;tabs&#39;)#get tabs collection</span></div><div class='line' id='LC285'><br/></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tab_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;tab_id&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC287'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span> <span class="o">=</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span> <span class="p">:</span> <span class="n">tab_id</span><span class="p">})</span></div><div class='line' id='LC288'><br/></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#whatever stevens json collection is called</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bill_json</span> <span class="o">=</span> <span class="n">get_db_collection</span><span class="p">(</span><span class="s">&#39;bill_json&#39;</span><span class="p">)</span></div><div class='line' id='LC291'><br/></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#Insert bill items to tab</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;items_prices&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">bill_json</span><span class="p">[</span><span class="s">&#39;tab_items&#39;</span><span class="p">]</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_tab</span><span class="p">[</span><span class="s">&#39;total&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">bill_json</span><span class="p">[</span><span class="s">&#39;tab_meta&#39;</span><span class="p">]</span></div><div class='line' id='LC295'><br/></div><div class='line' id='LC296'><br/></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC298'><br/></div><div class='line' id='LC299'><span class="c"># def send_email(subject, sender, recipients, text_body, html_body):</span></div><div class='line' id='LC300'><span class="c">#     msg = Message(subject, sender = sender, recipients = recipients)</span></div><div class='line' id='LC301'><span class="c">#     msg.body = text_body</span></div><div class='line' id='LC302'><span class="c">#     msg.html = html_body</span></div><div class='line' id='LC303'><span class="c">#     thr = Thread(target = send_async_email, args = [msg])</span></div><div class='line' id='LC304'><span class="c">#     thr.start()</span></div><div class='line' id='LC305'><br/></div><div class='line' id='LC306'><span class="c"># This route is expecting a parameter containing the name</span></div><div class='line' id='LC307'><span class="c"># of a file. Then it will locate that file on the upload</span></div><div class='line' id='LC308'><span class="c"># directory and show it on the browser, so if the user uploads</span></div><div class='line' id='LC309'><span class="c"># an image, that image is going to be show after the upload</span></div><div class='line' id='LC310'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/uploads/&lt;filename&gt;&#39;</span><span class="p">)</span></div><div class='line' id='LC311'><span class="k">def</span> <span class="nf">uploaded_file</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">send_from_directory</span><span class="p">(</span><span class="n">app</span><span class="o">.</span><span class="n">config</span><span class="p">[</span><span class="s">&#39;UPLOAD_FOLDER&#39;</span><span class="p">],</span> <span class="n">filename</span><span class="p">)</span></div><div class='line' id='LC313'><br/></div><div class='line' id='LC314'><span class="c">########################################################################</span></div><div class='line' id='LC315'><br/></div><div class='line' id='LC316'><br/></div><div class='line' id='LC317'><span class="c">############################## VENMO ###################################</span></div><div class='line' id='LC318'><br/></div><div class='line' id='LC319'><span class="c">### init</span></div><div class='line' id='LC320'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">)</span></div><div class='line' id='LC321'><span class="k">def</span> <span class="nf">index</span><span class="p">():</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">session</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;venmo_token&#39;</span><span class="p">):</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># return &#39;Your Venmo token is %s&#39; % session.get(&#39;venmo_token&#39;)</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># venmo_token  = session.get(&#39;venmo_token&#39;)</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># charge_or_pay(&#39;charge&#39;,venmo_token,8576009129, 0.01,&#39;&#39;)</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;Jaime charged&#39;</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">redirect</span><span class="p">(</span><span class="s">&#39;https://api.venmo.com/v1/oauth/authorize?client_id=</span><span class="si">%s</span><span class="s">&amp;scope=make_payments,access_profile&amp;response_type=code&#39;</span> <span class="o">%</span> <span class="n">CONSUMER_ID</span><span class="p">)</span></div><div class='line' id='LC329'><br/></div><div class='line' id='LC330'><br/></div><div class='line' id='LC331'><span class="c">#### Charge</span></div><div class='line' id='LC332'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/master_charge&#39;</span><span class="p">)</span></div><div class='line' id='LC333'><span class="k">def</span> <span class="nf">master_charge</span><span class="p">(</span><span class="n">master</span><span class="p">):</span></div><div class='line' id='LC334'>&nbsp;&nbsp;<span class="k">if</span> <span class="n">session</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;venmo_token&#39;</span><span class="p">):</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span> <span class="o">=</span> <span class="n">get_db_conection</span><span class="p">(</span><span class="s">&quot;okra&quot;</span><span class="p">)</span> <span class="c">#get conncection</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">users</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">users</span> <span class="c">#get tabs collection</span></div><div class='line' id='LC337'><br/></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">user</span> <span class="ow">in</span> <span class="n">users</span><span class="p">:</span></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user_id</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;user_id&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">le_user</span> <span class="o">=</span> <span class="n">tabs</span><span class="o">.</span><span class="n">find_one</span><span class="p">({</span><span class="s">&quot;id&quot;</span> <span class="p">:</span> <span class="n">user_id</span><span class="p">})</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">user_id</span> <span class="o">!=</span> <span class="s">&quot;&quot;</span><span class="p">):</span></div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">charge_or_pay</span><span class="p">(</span><span class="s">&#39;pay&#39;</span><span class="p">,</span> <span class="n">user</span><span class="o">.</span><span class="n">token</span><span class="p">,</span> <span class="n">master</span><span class="o">.</span><span class="n">phone</span><span class="p">,</span> <span class="n">master</span><span class="o">.</span><span class="n">amt</span><span class="p">,</span> <span class="n">user</span><span class="o">.</span><span class="n">note</span><span class="p">)</span></div><div class='line' id='LC343'><br/></div><div class='line' id='LC344'><br/></div><div class='line' id='LC345'><span class="c"># def add_venmo_user(phone_number,display_name, token):</span></div><div class='line' id='LC346'><br/></div><div class='line' id='LC347'><br/></div><div class='line' id='LC348'><br/></div><div class='line' id='LC349'><br/></div><div class='line' id='LC350'><span class="c">###### OAuth</span></div><div class='line' id='LC351'><br/></div><div class='line' id='LC352'><span class="nd">@app.route</span><span class="p">(</span><span class="s">&#39;/oauth-authorized&#39;</span><span class="p">)</span></div><div class='line' id='LC353'><span class="k">def</span> <span class="nf">oauth_authorized</span><span class="p">():</span></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">AUTHORIZATION_CODE</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;code&#39;</span><span class="p">)</span></div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">data</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;client_id&quot;</span><span class="p">:</span><span class="n">CONSUMER_ID</span><span class="p">,</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;client_secret&quot;</span><span class="p">:</span><span class="n">CONSUMER_SECRET</span><span class="p">,</span></div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;code&quot;</span><span class="p">:</span><span class="n">AUTHORIZATION_CODE</span></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">url</span> <span class="o">=</span> <span class="s">&quot;https://api.venmo.com/v1/oauth/access_token&quot;</span></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="n">requests</span><span class="o">.</span><span class="n">post</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response_dict</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">json</span><span class="p">()</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">access_token</span> <span class="o">=</span> <span class="n">response_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;access_token&#39;</span><span class="p">)</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="n">response_dict</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;user&#39;</span><span class="p">)</span></div><div class='line' id='LC365'><br/></div><div class='line' id='LC366'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">session</span><span class="p">[</span><span class="s">&#39;venmo_token&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">access_token</span></div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">session</span><span class="p">[</span><span class="s">&#39;venmo_username&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">user</span><span class="p">[</span><span class="s">&#39;username&#39;</span><span class="p">]</span></div><div class='line' id='LC368'><br/></div><div class='line' id='LC369'><br/></div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># phone_number = request.args.get(&#39;phone_number&#39;, &#39;&#39;)</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># print phone_number</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># user = {</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#         &#39;phone_number&#39; :   &#39;&#39;</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#     }</span></div><div class='line' id='LC375'><br/></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#return  &#39;fuck you %s&#39; % session[&#39;venmo_token&#39;]</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;You were signed in as </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">user</span><span class="p">[</span><span class="s">&#39;username&#39;</span><span class="p">]</span></div><div class='line' id='LC378'><span class="c">#########################################################################</span></div><div class='line' id='LC379'><br/></div><div class='line' id='LC380'><br/></div><div class='line' id='LC381'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">debug</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="s">&#39;0.0.0.0&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">80</span><span class="p">)</span></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.07594s from github-fe128-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-df9e4beac80276ed3dfa56be0d97b536d0f5ee12.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-22af5724b6a68093dc4ea24d753f84320ccb5dd5.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>


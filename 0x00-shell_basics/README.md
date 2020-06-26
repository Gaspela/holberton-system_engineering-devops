<article class="pending_logs">
        

  <div id="jigsaw-shortcut-lists">



</div>

<h1 class="gap">0x00. Shell, basics</h1>


<div id="project_id" style="display: none" data-project-id="205"></div>

<p class="sm-gap">
  <small>
    <i class="fa fa-folder-open"></i>
    Foundations - System engineering &amp; DevOps ― Bash
      &nbsp;
      <a id="block-modal-link" data-toggle="modal" data-target="#block-modal" href="#"><i class="fa fa-question-circle"></i></a>
  </small>
</p>

  <p>
    <em>
      <small>
        <i class="fa fa-user"></i> by Julien Barbier, co-founder at Holberton School
      </small>
    </em>
  </p>

  <p>
    <em>
      <small>
        <i class="fa fa-cogs"></i> weight: 1
      </small>
    </em>
  </p>



  <p>
    <small>
      <i class="fa fa-calendar"></i>
        Project over - took place from 09-11-2019 to 09-12-2019
        - you're done with <span id="student_task_done_percentage">200</span>% of tasks.
    </small>
  </p>



    <p>
      <small>
        <i class="fa fa-check-square"></i>
        QA review fully automated.
      </small>
    </p>

    <div class="gap clean well">
	<h4>In a nutshell…</h4>
	<ul>
		
		
			<li>
				<strong>Auto QA review:</strong>
					95.0/95 mandatory
						&amp;
						5.0/5 optional
			</li>
		<li>
			<strong>Altogether:</strong>
				&nbsp;<strong>200.0%</strong>
				<ul>
					<li>Mandatory: 100.0%</li>
					<li>Optional: 100.0%</li>
						<li>
							Calculation:&nbsp;
									100.0% + (100.0% * 100.0%)
							&nbsp;==&nbsp;<strong>200.0%</strong>
						</li>
				</ul>
		</li>
	</ul>
</div>
		







  <article id="description" class="gap formatted-content">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg" alt="" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/pn2_LGNuA1yFY7zy3CQmig" title="What Is &quot;The Shell&quot;?" target="_blank">What Is “The Shell”?</a> </li>
<li><a href="/rltoken/Hh8elGgCpj--6othR7S7GQ" title="Navigation" target="_blank">Navigation</a> </li>
<li><a href="/rltoken/84xsZOempqy5I7ZkueeIsg" title="Looking Around" target="_blank">Looking Around</a> </li>
<li><a href="/rltoken/Jp1c4V3hJiGBuVzYCtnQKw" title="A Guided Tour" target="_blank">A Guided Tour</a> </li>
<li><a href="/rltoken/wFwFXKQmSpmxYyvHvCIC-Q" title="Manipulating Files" target="_blank">Manipulating Files</a> </li>
<li><a href="/rltoken/Aq3NVLBhgnQS6NYtHI8i4w" title="Working With Commands" target="_blank">Working With Commands</a> </li>
<li><a href="/rltoken/RohkjGiQtMHgPfj0N_k1Bw" title="Reading Man pages" target="_blank">Reading Man pages</a> </li>
<li><a href="/rltoken/0HvJ2B_wSl6Oyshcn-OHrg" title="Keyboard shortcuts for Bash" target="_blank">Keyboard shortcuts for Bash</a> </li>
<li><a href="https://wiki.ubuntu.com/LTS" target="_blank">LTS</a></li>
<li><a href="/rltoken/ketzZf-802Fb-mSGkyPa4w" title="Shebang" target="_blank">Shebang</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>cd</code></li>
<li><code>ls</code></li>
<li><code>pwd</code></li>
<li><code>less</code></li>
<li><code>file</code></li>
<li><code>ln</code></li>
<li><code>cp</code></li>
<li><code>mv</code></li>
<li><code>rm</code></li>
<li><code>mkdir</code></li>
<li><code>type</code></li>
<li><code>which</code></li>
<li><code>help</code></li>
<li><code>man</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/VCja0ArJiqJAMEzE-01dSA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What does RTFM mean?</li>
<li>What is a Shebang</li>
</ul>

<h3>What is the Shell</h3>

<ul>
<li>What is the shell</li>
<li>What is the difference between a terminal and a shell</li>
<li>What is the shell prompt</li>
<li>How to use the history (the basics)</li>
</ul>

<h3>Navigation</h3>

<ul>
<li>What do the commands or built-ins <code>cd</code>, <code>pwd</code>, <code>ls</code> do </li>
<li>How to navigate the filesystem</li>
<li>What are the . and .. directories</li>
<li>What is the working directory, how to print it and how to change it</li>
<li>What is the root directory</li>
<li>What is the home directory, and how to go there</li>
<li>What is the difference between the root directory and the home directory of the user root</li>
<li>What are the characteristics of hidden files and how to list them</li>
<li>What does the command <code>cd -</code> do</li>
</ul>

<h3>Looking Around</h3>

<ul>
<li>What do the commands <code>ls</code>, <code>less</code>, <code>file</code> do</li>
<li>How do you use options and arguments with commands</li>
<li>Understand the ls long format and how to display it</li>
<li><a href="/rltoken/Jp1c4V3hJiGBuVzYCtnQKw" title="A Guided Tour" target="_blank">A Guided Tour</a></li>
<li>What does the <code>ln</code> command do</li>
<li>What do you find in the most common/important directories</li>
<li>What is a symbolic link</li>
<li>What is a hard link</li>
<li>What is the difference between a hard link and a symbolic link</li>
</ul>

<h3>Manipulating Files</h3>

<ul>
<li>What do the commands <code>cp</code>, <code>mv</code>, <code>rm</code>, <code>mkdir</code> do</li>
<li>What are wildcards and how do they work</li>
<li>How to use wildcards</li>
</ul>

<h3>Working with Commands</h3>

<ul>
<li>What do <code>type</code>, <code>which</code>, <code>help</code>, <code>man</code> commands do</li>
<li>What are the different kinds of commands</li>
<li>What is an alias</li>
<li>When do you use the command help instead of man</li>
</ul>

<h3>Reading Man Pages</h3>

<ul>
<li>How to read a man page</li>
<li>What are man page sections</li>
<li>What are the section numbers for User commands, System calls and Library functions</li>
</ul>

<h3>Keyboard Shortcuts for Bash</h3>

<ul>
<li>Common shortcuts for Bash</li>
</ul>

<h3>LTS</h3>

<ul>
<li>What does <code>LTS</code> mean?</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 14.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>$ wc -l file</code> should print 2)</li>
<li>All your files should end with a new line (<a href="http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789">why?</a>)</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>A <code>README.md</code> file at the root of the <code>holberton-system_engineering-devops</code> repo, containing a description of the repository</li>
<li>A <code>README.md</code> file, at the root of the folder of <em>this</em> project, describing what each script is doing</li>
<li>You are not allowed to use backticks, <code>&amp;&amp;</code>, <code>||</code> or <code>;</code></li>
<li>All your scripts must be executable. Use this command: <code>chmod u+x file</code>. We will see later what it means.</li>
</ul>

<h2>More Info</h2>

<p><i>Example of line count and first line</i></p>

<pre><code>julien@ubuntu:/tmp$ wc -l 12-file_type 
2 12-file_type
julien@ubuntu:/tmp$ head -n 1 12-file_type 
#!/bin/bash
julien@ubuntu:/tmp$ 
</code></pre>

<p>In order to test your scripts, you will need to use this command: <code>chmod u+x file</code>. We will see later what does <code>chmod</code> mean and do, but you can have a look at <code>man chmod</code> if you are curious.</p>

<p><i>Example</i></p>

<pre><code>julien@ubuntu:/tmp$ ls
12-file_type
lll
julien@ubuntu:/tmp$ ls -la lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ cat lll
#!/bin/bash
ls
julien@ubuntu:/tmp$ ls -l lll
-rw-rw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ chmod u+x lll # you do not have to understand this yet
julien@ubuntu:/tmp$ ls -l lll
-rwxrw-r-- 1 julien julien 15 Sep 19 21:05 lll
julien@ubuntu:/tmp$ ./lll
12-file_type
lll
julien@ubuntu:/tmp$ 
</code></pre>

  </article>

    <hr class="gap">
    <h2 class="gap">Quiz questions</h2>
    
      <p id="quiz_questions_collapse_toggle">Show</p>
    
    <section class="formatted-content quiz_questions_show_container" style="display: none;">
        <div class="quiz_question_item_container" data-role="quiz_question337" data-position="1">
          <div class=" clearfix" id="quiz_question-337">
    
    <h4 class="quiz_question">Question #0</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>What command would you use to list files on Linux?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="337">
                <li class="">
    <input type="checkbox" data-quiz-question-id="337" data-quiz-answer-id="1504590428218" disabled="">
    <p>pwd</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="337" data-quiz-answer-id="1504590430644" disabled="">
    <p>cd</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="337" data-quiz-answer-id="1504590432223" disabled="" checked="">
    <p>ls</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="337" data-quiz-answer-id="1504590435521" disabled="">
    <p>list</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="337" data-quiz-answer-id="1504590441025" disabled="">
    <p>which</p>

</li>



        </ul>

    <!-- Quiz question Tips -->

</div>

        </div>
        <div class="quiz_question_item_container" data-role="quiz_question338" data-position="2">
          <div class=" clearfix" id="quiz_question-338">
    
    <h4 class="quiz_question">Question #1</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>What does LTS stand for?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="338">
                <li class="">
    <input type="checkbox" data-quiz-question-id="338" data-quiz-answer-id="1504590453407" disabled="" checked="">
    <p>Long Term Support</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="338" data-quiz-answer-id="1504590473410" disabled="">
    <p>Long Time Support</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="338" data-quiz-answer-id="1504590515359" disabled="">
    <p>Last Terrible Service</p>

</li>



        </ul>

    <!-- Quiz question Tips -->

</div>

        </div>
        <div class="quiz_question_item_container" data-role="quiz_question339" data-position="3">
          <div class=" clearfix" id="quiz_question-339">
    
    <h4 class="quiz_question">Question #2</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>How do you change directory on Linux?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="339">
                <li class="">
    <input type="checkbox" data-quiz-question-id="339" data-quiz-answer-id="1504590536017" disabled="">
    <p>pwd</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="339" data-quiz-answer-id="1504590538875" disabled="" checked="">
    <p>cd</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="339" data-quiz-answer-id="1504590542475" disabled="">
    <p>ls</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="339" data-quiz-answer-id="1504590544749" disabled="">
    <p>which</p>

</li>



        </ul>

    <!-- Quiz question Tips -->

</div>

        </div>
        <div class="quiz_question_item_container" data-role="quiz_question340" data-position="4">
          <div class=" clearfix" id="quiz_question-340">
    
    <h4 class="quiz_question">Question #3</h4>

    <!-- Quiz question tags -->

    <!-- Quiz question Body -->
    <p>What does RTFM stand for?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="340">
                <li class="">
    <input type="checkbox" data-quiz-question-id="340" data-quiz-answer-id="1504590550182" disabled="">
    <p>Remember The First Manipulation</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="340" data-quiz-answer-id="1504590564292" disabled="">
    <p>Read, Teach, Forget, Migrate</p>

</li>



                <li class="">
    <input type="checkbox" data-quiz-question-id="340" data-quiz-answer-id="1504590566251" disabled="" checked="">
    <p>Read The F** Manual</p>

</li>



        </ul>

    <!-- Quiz question Tips -->

</div>

        </div>

    </section>



    <!-- Servers -->

    <!-- Tasks -->
      <hr class="gap">
      <h2 class="gap">Tasks</h2>
      <section class="formatted-content">
            <div data-role="task3" data-position="1">
              <div class=" clearfix gap" id="task-3">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="3">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="3" data-project-id="205" data-toggle="modal" data-target="#task-3-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-3-users-done-modal" data-task-id="3" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "0. Where am I?"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    0. Where am I?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="3" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Write a script that prints the absolute path name of the current working directory.</p>

<p>Example:</p>

<pre><code>$ ./0-current_working_directory
/Users/holbertonschool/holbertonschool-sysadmin_devops/0x00-shell_basics
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>0-current_working_directory</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="3" data-toggle="modal" data-target="#task-3-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-3-whiteboard-modal" data-task-id="3">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "0. Where am I?"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="3" data-toggle="modal" data-target="#task-test-correction-3-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-3-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "0. Where am I?"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="3" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="3">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="3">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="3">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="3" data-toggle="modal" data-target="#task-qa-review-3-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-3-modal" data-correction-id="49090" data-task-id="3">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">0. Where am I?</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task11" data-position="2">
              <div class=" clearfix gap" id="task-11">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="11">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="11" data-project-id="205" data-toggle="modal" data-target="#task-11-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-11-users-done-modal" data-task-id="11" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "1. What’s in there?"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    1. What’s in there?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="11" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Display the contents list of your current directory.</p>

<p>Example:</p>

<pre><code>$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>1-listit</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="11" data-toggle="modal" data-target="#task-11-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-11-whiteboard-modal" data-task-id="11">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "1. What’s in there?"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="11" data-toggle="modal" data-target="#task-test-correction-11-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-11-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "1. What’s in there?"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="11" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="11">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="11">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="11">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="11" data-toggle="modal" data-target="#task-qa-review-11-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-11-modal" data-correction-id="49090" data-task-id="11">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">1. What’s in there?</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task748" data-position="3">
              <div class=" clearfix gap" id="task-748">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="748">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="748" data-project-id="205" data-toggle="modal" data-target="#task-748-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-748-users-done-modal" data-task-id="748" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "2. There is no place like home"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    2. There is no place like home
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="748" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Write a script that changes the working directory to the user’s home directory.</p>

<ul>
<li>You are not allowed to use any shell variables</li>
</ul>

<pre><code>julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ echo $HOME
/home/julien
julien@ubuntu:/tmp$ source ./2-bring_me_home
julien@ubuntu:~$ pwd
/home/julien
julien@ubuntu:~$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>2-bring_me_home</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="748" data-toggle="modal" data-target="#task-748-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-748-whiteboard-modal" data-task-id="748">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "2. There is no place like home"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="748" data-toggle="modal" data-target="#task-test-correction-748-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-748-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "2. There is no place like home"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="748" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="748">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="748">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="748">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="748" data-toggle="modal" data-target="#task-qa-review-748-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-748-modal" data-correction-id="49090" data-task-id="748">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">2. There is no place like home</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task17" data-position="4">
              <div class=" clearfix gap" id="task-17">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="17">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="17" data-project-id="205" data-toggle="modal" data-target="#task-17-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-17-users-done-modal" data-task-id="17" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "3. The long format"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    3. The long format
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="17" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Display current directory contents in a long format</p>

<p>Example:</p>

<pre><code>$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>3-listfiles</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="17" data-toggle="modal" data-target="#task-17-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-17-whiteboard-modal" data-task-id="17">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "3. The long format"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="17" data-toggle="modal" data-target="#task-test-correction-17-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-17-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "3. The long format"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="17" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="17">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="17">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="17">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="17" data-toggle="modal" data-target="#task-qa-review-17-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-17-modal" data-correction-id="49090" data-task-id="17">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">3. The long format</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task25" data-position="5">
              <div class=" clearfix gap" id="task-25">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="25">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="25" data-project-id="205" data-toggle="modal" data-target="#task-25-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-25-users-done-modal" data-task-id="25" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "4. Hidden files"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    4. Hidden files
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="25" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Display current directory contents, including hidden files (starting with <code>.</code>). Use the long format.</p>

<p>Example:</p>

<pre><code>$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>4-listmorefiles</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="25" data-toggle="modal" data-target="#task-25-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-25-whiteboard-modal" data-task-id="25">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "4. Hidden files"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="25" data-toggle="modal" data-target="#task-test-correction-25-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-25-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "4. Hidden files"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="25" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="25">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="25">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="25">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="25" data-toggle="modal" data-target="#task-qa-review-25-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-25-modal" data-correction-id="49090" data-task-id="25">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">4. Hidden files</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task18" data-position="6">
              <div class=" clearfix gap" id="task-18">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="18">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="18" data-project-id="205" data-toggle="modal" data-target="#task-18-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-18-users-done-modal" data-task-id="18" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "5. I love numbers"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    5. I love numbers
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="18" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Display current directory contents.</p>

<ul>
<li>Long format</li>
<li>with user and group IDs displayed numerically</li>
<li>And hidden files (starting with .)</li>
</ul>

<p>Example:</p>

<pre><code>$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>5-listfilesdigitonly</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="18" data-toggle="modal" data-target="#task-18-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-18-whiteboard-modal" data-task-id="18">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "5. I love numbers"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="18" data-toggle="modal" data-target="#task-test-correction-18-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-18-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "5. I love numbers"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="18" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="18">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="18">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="18">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="18" data-toggle="modal" data-target="#task-qa-review-18-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-18-modal" data-correction-id="49090" data-task-id="18">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">5. I love numbers</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task20" data-position="7">
              <div class=" clearfix gap" id="task-20">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="20">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="20" data-project-id="205" data-toggle="modal" data-target="#task-20-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-20-users-done-modal" data-task-id="20" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "6. Welcome holberton"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    6. Welcome holberton
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="20" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Create a script that creates a directory named <code>holberton</code> in the <code>/tmp/</code> directory.</p>

<p>Example:</p>

<pre><code>$ ./6-firstdirectory
$ file /tmp/holberton/
/tmp/holberton/: directory
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>6-firstdirectory</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="20" data-toggle="modal" data-target="#task-20-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-20-whiteboard-modal" data-task-id="20">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "6. Welcome holberton"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="20" data-toggle="modal" data-target="#task-test-correction-20-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-20-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "6. Welcome holberton"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="20" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="20">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="20">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="20">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="20" data-toggle="modal" data-target="#task-qa-review-20-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-20-modal" data-correction-id="49090" data-task-id="20">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">6. Welcome holberton</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task21" data-position="8">
              <div class=" clearfix gap" id="task-21">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="21">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="21" data-project-id="205" data-toggle="modal" data-target="#task-21-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-21-users-done-modal" data-task-id="21" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "7. Betty in Holberton"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    7. Betty in Holberton
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="21" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Move the file <code>betty</code> from <code>/tmp/</code> to <code>/tmp/holberton</code>.</p>

<p>Example:</p>

<pre><code>$ ./7-movethatfile
$ ls /tmp/holberton/
betty
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>7-movethatfile</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="21" data-toggle="modal" data-target="#task-21-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-21-whiteboard-modal" data-task-id="21">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "7. Betty in Holberton"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="21" data-toggle="modal" data-target="#task-test-correction-21-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-21-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "7. Betty in Holberton"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="21" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="21">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="21">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="21">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="21" data-toggle="modal" data-target="#task-qa-review-21-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-21-modal" data-correction-id="49090" data-task-id="21">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">7. Betty in Holberton</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task22" data-position="9">
              <div class=" clearfix gap" id="task-22">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="22">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="22" data-project-id="205" data-toggle="modal" data-target="#task-22-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-22-users-done-modal" data-task-id="22" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "8. Bye bye Betty"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    8. Bye bye Betty
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="22" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Delete the file <code>betty</code>.</p>

<ul>
<li>The file <code>betty</code> is in <code>/tmp/holberton</code></li>
</ul>

<p>Example:</p>

<pre><code>$ ./8-firstdelete
$ ls /tmp/holberton/
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>8-firstdelete</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="22" data-toggle="modal" data-target="#task-22-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-22-whiteboard-modal" data-task-id="22">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "8. Bye bye Betty"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="22" data-toggle="modal" data-target="#task-test-correction-22-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-22-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "8. Bye bye Betty"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="22" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="22">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="22">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="22">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="22" data-toggle="modal" data-target="#task-qa-review-22-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-22-modal" data-correction-id="49090" data-task-id="22">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">8. Bye bye Betty</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task23" data-position="10">
              <div class=" clearfix gap" id="task-23">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="23">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="23" data-project-id="205" data-toggle="modal" data-target="#task-23-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-23-users-done-modal" data-task-id="23" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "9. Bye bye Holberton"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    9. Bye bye Holberton
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="23" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Delete the directory <code>holberton</code> that is in the <code>/tmp</code> directory.</p>

<p>Example:</p>

<pre><code>$ ./9-firstdirdeletion
$ file /tmp/holberton
/tmp/holberton: cannot open `/tmp/holberton' (No such file or directory)
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>9-firstdirdeletion</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="23" data-toggle="modal" data-target="#task-23-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-23-whiteboard-modal" data-task-id="23">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "9. Bye bye Holberton"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="23" data-toggle="modal" data-target="#task-test-correction-23-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-23-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "9. Bye bye Holberton"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="23" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="23">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="23">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="23">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="23" data-toggle="modal" data-target="#task-qa-review-23-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-23-modal" data-correction-id="49090" data-task-id="23">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">9. Bye bye Holberton</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task749" data-position="11">
              <div class=" clearfix gap" id="task-749">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="749">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="749" data-project-id="205" data-toggle="modal" data-target="#task-749-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-749-users-done-modal" data-task-id="749" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "10. Back to the future"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    10. Back to the future
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="749" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Write a script that changes the working directory to the previous one.</p>

<pre><code>julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>10-back</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="749" data-toggle="modal" data-target="#task-749-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-749-whiteboard-modal" data-task-id="749">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "10. Back to the future"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="749" data-toggle="modal" data-target="#task-test-correction-749-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-749-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "10. Back to the future"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="749" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="749">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="749">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="749">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="749" data-toggle="modal" data-target="#task-qa-review-749-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-749-modal" data-correction-id="49090" data-task-id="749">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">10. Back to the future</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task750" data-position="12">
              <div class=" clearfix gap" id="task-750">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="750">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="750" data-project-id="205" data-toggle="modal" data-target="#task-750-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-750-users-done-modal" data-task-id="750" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "11. Lists"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    11. Lists
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="750" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the <code>/boot</code> directory (in this order), in long format.</p>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>11-lists</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="750" data-toggle="modal" data-target="#task-750-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-750-whiteboard-modal" data-task-id="750">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "11. Lists"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="750" data-toggle="modal" data-target="#task-test-correction-750-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-750-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "11. Lists"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="750" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="750">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="750">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="750">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="750" data-toggle="modal" data-target="#task-qa-review-750-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-750-modal" data-correction-id="49090" data-task-id="750">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">11. Lists</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task751" data-position="13">
              <div class=" clearfix gap" id="task-751">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="751">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="751" data-project-id="205" data-toggle="modal" data-target="#task-751-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-751-users-done-modal" data-task-id="751" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "12. File type"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    12. File type
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="751" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Write a script that prints the type of the file named <code>iamafile</code>. The file <code>iamafile</code> will be in the <code>/tmp</code> directory when we will run your script.</p>

<p>Example</p>

<pre><code>ubuntu@ip-172-31-63-244:~$ ./12-file_type
/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
</code></pre>

<p>Note that depending on the file, the output of your script will be different.</p>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>12-file_type</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="751" data-toggle="modal" data-target="#task-751-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-751-whiteboard-modal" data-task-id="751">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "12. File type"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="751" data-toggle="modal" data-target="#task-test-correction-751-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-751-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "12. File type"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="751" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="751">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="751">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="751">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="751" data-toggle="modal" data-target="#task-qa-review-751-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-751-modal" data-correction-id="49090" data-task-id="751">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">12. File type</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task752" data-position="14">
              <div class=" clearfix gap" id="task-752">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="752">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="752" data-project-id="205" data-toggle="modal" data-target="#task-752-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-752-users-done-modal" data-task-id="752" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "13. We are symbols, and inhabit symbols"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    13. We are symbols, and inhabit symbols
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="752" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Create a symbolic link to <code>/bin/ls</code>, named <code>__ls__</code>.
The symbolic link should be created in the current working directory. </p>

<pre><code>ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
ubuntu@ip-172-31-63-244:/tmp/sym$./13-symbolic_link
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -&gt; /bin/ls
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>13-symbolic_link</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="752" data-toggle="modal" data-target="#task-752-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-752-whiteboard-modal" data-task-id="752">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "13. We are symbols, and inhabit symbols"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="752" data-toggle="modal" data-target="#task-test-correction-752-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-752-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "13. We are symbols, and inhabit symbols"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="752" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="752">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="752">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="752">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="752" data-toggle="modal" data-target="#task-qa-review-752-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-752-modal" data-correction-id="49090" data-task-id="752">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">13. We are symbols, and inhabit symbols</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task753" data-position="15">
              <div class=" clearfix gap" id="task-753">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="753">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="753" data-project-id="205" data-toggle="modal" data-target="#task-753-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-753-users-done-modal" data-task-id="753" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "14. Copy HTML files"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    14. Copy HTML files
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="753" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.</p>

<p>You can consider that all HTML files have the extension <code>.html</code></p>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>14-copy_html</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="753" data-toggle="modal" data-target="#task-753-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-753-whiteboard-modal" data-task-id="753">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "14. Copy HTML files"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="753" data-toggle="modal" data-target="#task-test-correction-753-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-753-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "14. Copy HTML files"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="753" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="753">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="753">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="753">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="753" data-toggle="modal" data-target="#task-qa-review-753-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-753-modal" data-correction-id="49090" data-task-id="753">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">14. Copy HTML files</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task754" data-position="16">
              <div class=" clearfix gap" id="task-754">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="754">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="754" data-project-id="205" data-toggle="modal" data-target="#task-754-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-754-users-done-modal" data-task-id="754" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "15. Let’s move"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    15. Let’s move
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="754" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Create a script that moves all files beginning with an uppercase letter to the directory <code>/tmp/u</code>.</p>

<p>You can assume that the directory <code>/tmp/u</code> will exist when we will run your script</p>

<pre><code>ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Holberton
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -&gt; /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Notrebloh
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
ubuntu@ip-172-31-63-244:/tmp/sym$ ./15-lets_move
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -&gt; /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Holberton
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Notrebloh
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>15-lets_move</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="754" data-toggle="modal" data-target="#task-754-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-754-whiteboard-modal" data-task-id="754">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "15. Let’s move"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="754" data-toggle="modal" data-target="#task-test-correction-754-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-754-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "15. Let’s move"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="754" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="754">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="754">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="754">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="754" data-toggle="modal" data-target="#task-qa-review-754-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-754-modal" data-correction-id="49090" data-task-id="754">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">15. Let’s move</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task755" data-position="17">
              <div class=" clearfix gap" id="task-755">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="755">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="755" data-project-id="205" data-toggle="modal" data-target="#task-755-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-755-users-done-modal" data-task-id="755" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "16. Clean Emacs"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    16. Clean Emacs
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="755" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Create a script that deletes all files in the current working directory that end with the character <code>~</code>.</p>

<pre><code>ubuntu@ip-172-31-63-244:/tmp/sym$ ls
main.c  main.c~  Makefile~
ubuntu@ip-172-31-63-244:/tmp/sym$ ./16-clean_emacs
ubuntu@ip-172-31-63-244:/tmp/emacs$ ls
main.c
ubuntu@ip-172-31-63-244:/tmp/emacs$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>16-clean_emacs</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="755" data-toggle="modal" data-target="#task-755-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-755-whiteboard-modal" data-task-id="755">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "16. Clean Emacs"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="755" data-toggle="modal" data-target="#task-test-correction-755-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-755-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "16. Clean Emacs"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="755" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="755">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="755">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="755">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="755" data-toggle="modal" data-target="#task-qa-review-755-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-755-modal" data-correction-id="49090" data-task-id="755">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">16. Clean Emacs</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task756" data-position="18">
              <div class=" clearfix gap" id="task-756">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="756">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="756" data-project-id="205" data-toggle="modal" data-target="#task-756-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-756-users-done-modal" data-task-id="756" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "17. Tree"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    17. Tree
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="756" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Create a script that creates the directories <code>welcome/</code>, <code>welcome/to/</code> and <code>welcome/to/holberton</code> in the current directory.</p>

<p>You are only allowed to use two spaces in your script, not more.</p>

<pre><code>julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 44 Sep 20 12:09 17-tree
julien@ubuntu:/tmp/h$ wc -l 17-tree 
2 17-tree
julien@ubuntu:/tmp/h$ head -1 17-tree 
#!/bin/bash
julien@ubuntu:/tmp/h$ tr -cd ' ' &lt; 17-tree | wc -c # you do not have to understand this yet, but the result should be 2, 1 or 0
2
julien@ubuntu:/tmp/h$ ./17-tree 
julien@ubuntu:/tmp/h$ ls
17-tree  welcome
julien@ubuntu:/tmp/h$ ls welcome/
to
julien@ubuntu:/tmp/h$ ls -l welcome/to
total 4
drwxrwxr-x 2 julien julien 4096 Sep 20 12:11 holberton
julien@ubuntu:/tmp/h$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>17-tree</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="756" data-toggle="modal" data-target="#task-756-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-756-whiteboard-modal" data-task-id="756">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "17. Tree"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="756" data-toggle="modal" data-target="#task-test-correction-756-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-756-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "17. Tree"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="756" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="756">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="756">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="756">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="756" data-toggle="modal" data-target="#task-qa-review-756-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-756-modal" data-correction-id="49090" data-task-id="756">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">17. Tree</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task37" data-position="19">
              <div class=" clearfix gap" id="task-37">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="37">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="37" data-project-id="205" data-toggle="modal" data-target="#task-37-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-37-users-done-modal" data-task-id="37" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "18. Life is a series of commas, not periods"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    18. Life is a series of commas, not periods
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="37" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Write a command that lists all the files and directories of the current directory, separated by commas (<code>,</code>).</p>

<ul>
<li>Directory names should end with a slash (<code>/</code>)<br></li>
<li>Files and directories starting with a dot (<code>.</code>) should be listed<br></li>
<li>The listing should be alpha ordered, except for the directories <code>.</code> and <code>..</code> which should be listed at the very beginning</li>
<li>Only digits and letters are used to sort; Digits should come first</li>
<li>You can assume that all the files we will test with will have at least one letter or one digit</li>
<li>The listing should end with a new line<br></li>
</ul>

<pre><code>ubuntu@ip-172-31-63-244:~/holbertonschool$ ls -a

.  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var

ubuntu@ip-172-31-63-244:~/holbertonschool$ ./18-commas

./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var

ubuntu@ip-172-31-63-244:~/holbertonschool$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>18-commas</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="37" data-toggle="modal" data-target="#task-37-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-37-whiteboard-modal" data-task-id="37">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "18. Life is a series of commas, not periods"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="37" data-toggle="modal" data-target="#task-test-correction-37-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-37-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "18. Life is a series of commas, not periods"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="37" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="37">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="37">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="37">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="37" data-toggle="modal" data-target="#task-qa-review-37-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-37-modal" data-correction-id="49090" data-task-id="37">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">18. Life is a series of commas, not periods</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
            <div data-role="task757" data-position="20">
              <div class=" clearfix gap" id="task-757">
<span id="user_id" data-id="1237"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default yes" data-task-id="757">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="757" data-project-id="205" data-toggle="modal" data-target="#task-757-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-757-users-done-modal" data-task-id="757" data-project-id="205">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "19. File type: Holberton"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    19. File type: Holberton
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>

  

  <!-- Progress vs Score -->
    <div class="task_progress_score_bar light_text" data-task-id="757" data-correction-id="49090">
      <div class="task_progress_bar" style="width: 100%;">
        <div class="task_score_bar" style="width: 100%;">
        </div>
      </div>
      <div class="task_progress_score_text">
        Score: <span class="task_score_value">100.00%</span> (<span class="task_progress_value">Checks completed: 100.00%</span>)
      </div>
    </div>

  <!-- Task Body -->
  <p>Create a magic file <code>holberton.mgc</code> that can be used with the command <code>file</code> to detect <code>Holberton</code> data files. <code>Holberton</code> data files always contain the string <code>HOLBERTON</code> at offset 0.</p>

<p><strong>holberton.mgc has to be created on Ubuntu 14.04 LTS</strong></p>

<pre><code>ubuntu@ip-172-31-63-244:/tmp/magic$ cp /bin/ls .
ubuntu@ip-172-31-63-244:/tmp/magic$ ls -la
total 268
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 02:44 .
drwxrwxrwt 11 root   root   139264 Sep 20 02:44 ..
-rw-r--r--  1 ubuntu ubuntu    496 Sep 20 02:42 holberton.mgc
-rwxr-xr-x  1 ubuntu ubuntu 110080 Sep 20 02:43 ls
-rw-rw-r--  1 ubuntu ubuntu     50 Sep 20 02:06 thisisanholbertonfile
-rw-rw-r--  1 ubuntu ubuntu     30 Sep 20 02:16 thisisatextfile
ubuntu@ip-172-31-63-244:/tmp/magic$ file --mime-type -m holberton.mgc *
holberton.mgc:         application/octet-stream
ls:                    application/octet-stream
thisisanholbertonfile: Holberton
thisisatextfile:       text/plain
ubuntu@ip-172-31-63-244:/tmp/magic$ file -m holberton.mgc *
holberton.mgc:         data
ls:                    data
thisisanholbertonfile: Holberton data
thisisatextfile:       ASCII text
ubuntu@ip-172-31-63-244:/tmp/magic$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x00-shell_basics</code></li>
        <li>File: <code>holberton.mgc</code></li>
    </ul>



    <div class="student_correction_requests">
      <!-- DISABLE UNTIL MIGRATION
        <button class="task_whiteboard_modal btn btn-default size_three" data-task-id="757" data-toggle="modal" data-target="#task-757-whiteboard-modal">
          Whiteboard
        </button>
        <div class="modal fade task_whiteboard_modal" id="task-757-whiteboard-modal" data-task-id="757">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Your Notes on "19. File type: Holberton"</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="task-note-prompts-and-placeholders-container">
                    <button type="button" class="whiteboard-submit-button btn btn-primary">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>

      -->

      <!-- Button test code -->
        <button class="task_correction_modal btn btn-default size_three" data-task-id="757" data-toggle="modal" data-target="#task-test-correction-757-correction-modal">
          Check your code?
        </button>
        <div class="modal fade task_correction_modal student_modal" id="task-test-correction-757-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">Correction of "19. File type: Holberton"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="757" data-type="">
                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>


                            <div class="cta-button" data-task-id="757">&lt; <a href="#">Learn more about this flag</a> &gt;</div>
                            <div class="event-footer" style="display: none;">
                                <div class="cta-image"></div>
                                <div class="cta-title"></div>
                                <div class="cta-text"></div>
                                <p class="cta-source">Source: <a target="_blank" href="https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/">https://www.cosmopolitan.com/sex-love/a31743384/lgbtq-pride-flags-guide/</a></p>
                            </div>
                    </center>
                </div>
                <div class="result"></div>
                    <div class="post-check-message">
                        <p></p>
                        <a href="https://twitter.com/hashtag/Pride2020" target="_blank">
                            <img src="/assets/pride-hbtn-8cd5d1f46994096eab0b578260896b529f3055d04dad3fce116ce6798bc948a7.png" alt="Pride hbtn">
                        </a>
                    </div>
                <div class="help">
                    <button data-task-id="757">
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </button>
                    <div class="help-container" data-task-id="757">
                        <div class="check-line">
                            <div class="check-inline requirement success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Requirement success
                            </div>
                            <div class="check-inline requirement fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Requirement fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline code success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Code success
                            </div>
                            <div class="check-inline code fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Code fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline efficiency success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Efficiency success
                            </div>
                            <div class="check-inline efficiency fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Efficiency fail
                            </div>
                        </div>
                        <div class="check-line">
                            <div class="check-inline answer success">
                                <i class="fa fa-check" aria-hidden="true"></i>
                                Text answer success
                            </div>
                            <div class="check-inline answer fail">
                                <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
                                Text answer fail
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div>

        


      <!-- Button containers -->

      <!-- Button for QA Review -->
        <button class="task_get_qa_review btn btn-default size_three" data-task-id="757" data-toggle="modal" data-target="#task-qa-review-757-modal">
          QA Review
        </button>
        <div class="modal fade task_get_qa_review" id="task-qa-review-757-modal" data-correction-id="49090" data-task-id="757">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                <h4 class="modal-title">19. File type: Holberton</h4>
            </div>
            <div class="modal-body">
                <div class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="review-container">
                    <div class="review-corrector"></div>
                    <div class="review-github"></div>
                    <div class="review-percentage_down"></div>
                    <ul class="review-checks list-group sm-gap"></ul>
                    <div class="review-comment"></div>
                </div>
            </div>
        </div>
    </div>
</div>

    </div>


</div>
 
            </div>
      </section>






  <div class="modal fade" id="block-modal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
        <h4 class="modal-title">About the "Bash" block</h4>
      </div>
      <div class="modal-body">
        <p>Unless stated, all your projects will be auto-corrected with Ubuntu 14.04 LTS.</p>

      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->






      </article>

---
[![MIT License](https://raw.github.com/initbrain/intelwiz/master/intelwiz/images/logo_mit.png)](http://opensource.org/licenses/MIT)  
[MIT License](http://opensource.org/licenses/MIT)

---

Intelligence Wizard
===================

*   **State:**

    This is a Proof of Concept... Interactive FlowChart in Python !  
    Changes may occur in the future ;)


*   **Description:**

    This project start with a poor number of final implemented fonctionnalites, just keep in mind that we want to make easier to visualise and construct, not just to automate.

    Ok, so this thing automate actions, right? Yes, but it's not the only goal... Imagine a basic artificial intelligence, what is it made of?  
    One can imagine a spider web containing a few nodes to access various possibilities, in fact, some ways that it can use to evaluate his environnement and evolve in it. Now rethink about this tool, it can visualy illustrate action status and what it manipule and how. It's like a backdoor inside the spider ;)

    For now like I said, "this project start with a poor number of final implemented fonctionnalites" and it just contain some colors around graph nodes to represent their status, we can froze a node like a request to a webserver, this can help to stay off the blacklist of a free webservice for exemple (by keeping sourcecode, HTTP headers, etc).

    Flowcharts backups (.fc) keeps the frozen status usable, you can save any observed behaviours and reload it later.  
    To froze / unfroze a node, press the corresponding "F" button inside the treeview (the left part of the GUI).  
    To access actions (add, remove, export) on the graph, press right clic on it.  
    For now only three interesting fonctionnalities:
    * Add Node - Web - GetSource
    * Add Node - Data - PythonEval
    * Add Node - Input - TextEdit  
    (others are from default library goals)

    Ok, I'm probably so proud that I may have missed one thing again, so many ideas and not the time to realise or simply assess the relevance. Suggestions / comments are appreciated at <contact@free-knowledge.net>.


*   **Screenshot:**

    ![Intelligence Wizard](https://raw.githubusercontent.com/initbrain/intelwiz/master/intelwiz/images/demo_webparsing.png)


*   **Installation ($: user, #: root):**

    We have included our own installation wizard.  
    It require the installation of the following dependencies:

        # apt-get install git python-setuptools python-pip

    The full git repository is at: <https://github.com/initbrain/intelwiz.git>  
    Get it using the following command:

        $ git clone git://github.com/initbrain/intelwiz.git

    And proceed to final steps:

        $ cd intelwiz/
        # python setup.py install

    To use the tool, launch it with this alias:

        $ intelwiz


*   **TODO list:**

    *   Make a nice description :)
    *   Add a real right part (save output, export json, etc)
    *   Remove "zoom out" event at flowchart import (.fc)
    *   Support loops in flowcharts
    *   Add some features


Do not hesitate to send us your suggestions / comments at: <contact@free-knowledge.net> :)

from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Marcel", "Hallgarten"]
    email = "marcel.hallgarten@uni-tuebingen.de"
    twitter = "MHallgarten0797"
    github = "mh0797"
    linkedin = "marcel-hallgarten-441412226"
    bio_text = f"""
                <p>
                    Hi, I'm a PhD student specializing in machine learning-based behavior planning for autonomous driving.
                </p>
                <p>
                    <span style="font-weight: bold;">Interests:</span>
                    I'm particularly interested in robust imitation learning, which involves training an autonomous vehicle to imitate expert drivers and learn from their behavior in order to navigate complex traffic scenarios safely and efficiently.
                </p>
                <p>
                    <span style="font-weight: bold;">Bio:</span>
                    I received my B.Sc. in Mechanical Engineering in 2019 at <a href="https://www.mach.kit.edu">Karlsruhe Institute of Technology (KIT)</a> as one of the best four graduates of the year.
                    M.Sc. was centered around machine learning, machine vision and vehicle dynamics and I graduated in 2021 with distinction. 
                    In 2021 I started my PhD in Computer Science at <a href="https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/kognitive-systeme/">University of Tübingen</a>
                    under the supervision of <a href="https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/kognitive-systeme/the-chair/staff/prof-dr-andreas-zell/">Prof. Dr. Andreas Zell</a>
                    and in collaboration with <a href="https://www.bosch.com/research/">Bosch Corporate Resarch</a>.

                </p>
                <p>For any inquiries, feel free to reach out to me via mail!</p>
                <p>
                    <a href="mailto:marcel.hallgarten@uni-tuebingen.de" style="margin-right: 5px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/MHallgarten0797" target="_blank" style="margin-right: 5px"><i class="fab fa-x-twitter fa-lg"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=we6nXHoAAAAJ&hl=en&oi=ao" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/mh0797" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/marcel-hallgarten-441412226" target="_blank" style="margin-right: 5px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#demo" data-toggle="collapse" style="margin-left: -6px; margin-top: -2px;"><i class="fa-solid fa-trophy"></i>Awards</button>
                    <div id="demo" class="collapse">
                        <span style="font-weight: bold;">Awards:</span>
                        In 2015, I graduated among the top five of my year from secondary school and received <a href="https://www.e-fellows.net/" target="_blank">the e-fellows scholarship</a> and was admitted to <a href="https://www.dpg-physik.de/" target="_blank">the German Physics Society</a>.
                        In 2019 I received the Grashof award for Academic Excellence for my Bachelor's degree. Moreover, my Master"s degree was obtained with distinction.
                        During my PhD studies, I won the 2023 <a href="https://opendrivelab.com/challenge2023/">nuPlan Competition</a> hosted at CVPR Workshop End-to-End Autonomous Driving: Emerging Tasks and Challenges.
                        As part of my PhD journey with Bosch, I participated in the first <a href="https://www.linkedin.com/posts/bosch-research_boschresearchfamily-phd-scienceslam-activity-7112434706515652609-huof/">Bosch PhD Science Slam</a>, where I was among the five finalists.
                        In addition, I won the <a href="https://www.marga.net">Marga Business Simulation</a> with my team of fellow Bosch PhD students in 2024.
                    </div>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                    This page is based on the template of <a href="https://m-niemeyer.github.io/" target="_blank">Michael Niemeyer</a>. Checkout his <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">GitHub repository</a> for instructions on how to use it.<br>
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        'Andreas Geiger': 'https://www.cvlibs.net/',
        'Kashyap Chitta': 'https://kashyap7x.github.io',
        'Daniel Dauner': 'https://danieldauner.github.io/',
        'Xinshuo Weng': 'https://research.nvidia.com/person/xinshuo-weng',
        'Zhiyu Huang': 'https://mczhi.github.io/',
        'Zetong Yang': 'https://scholar.google.com/citations?user=oPiZSVYAAAAJ&hl=zh-CN',
        'Igor Gilitschenski': 'https://www.gilitschenski.org/igor/',
        'Boris Ivanovic': 'https://www.borisivanovic.com/',
        'Marco Pavone': 'https://web.stanford.edu/~pavone/',
        'Katrin Renz': 'https://www.katrinrenz.de/',
        'Hongyang Li': 'https://lihongyang.info/',
        'Tianyu Li': 'https://www.linkedin.com/in/sephy-li/',
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Marcel Hallgarten', 
                         add_links=True, equal_contribution=None):
    links = get_author_dict() if add_links else {}
    s = ""

    equal_contributors = -1
    if equal_contribution is not None:
        equal_contributors = equal_contribution
    for idx, p in enumerate(persons):
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if idx < equal_contributors:
            string_part_i += "*"
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s


def get_paper_entry(entry_key, entry):
    if 'highlight' in entry.fields.keys():
        s = """<div style="background-color: #ffffd0; margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    else:
        s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""

    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""

    if 'equal_contribution' in entry.fields.keys():
        s += f"""{generate_person_html(entry.persons['author'], equal_contribution=int(entry.fields['equal_contribution']))} <br>"""
    else: 
        s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Abs', 'pdf': 'Paper', 'supp': 'Supplementary', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    
    cite = "<pre><code>@" + entry.type + "{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_teaching_entry(entry_key, entry):
    imgs={
        "seminar": "assets/img/teaching/seminar.svg",
        "lecture": "assets/img/teaching/lecture.svg",
    }
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-1">"""
    s += f"""<img src="{imgs[entry.fields['type'].lower()]}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-11">"""

    artefacts = ['year', 'type', 'course', 'institution', 'desc']
    assert all([k in entry.fields.keys() for k in artefacts]), f'Teaching entry must contain {artefacts}, but got {entry.fields.keys()}'
    s += f"""{entry.fields['type']}: <span style="font-weight: bold;">{entry.fields['course']}</span><br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['institution']}</span>, {entry.fields['year']}<br>"""

    course_id = entry.fields['course'].replace(' ', '_').lower() + '_' + entry.fields['year']
    s += f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#{course_id}" data-toggle="collapse" style="margin-left: -6px; margin-top: -2px;"><i class="fa-regular fa-file-lines"></i> Description</button>"""
    s += f"""<div id="{course_id}" class="collapse">
        {entry.fields['desc']}
    </div>"""

    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_teaching_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('teaching_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_teaching_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    teaching = get_teaching_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer">
  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                    <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    </div>
                    <br>
                    <div class="col-md-8" style="">
                        {bio_text}
                    </div>
                    <div class="col-md-4" style="">
                        <img src="assets/img/profile.jpg" class="img-thumbnail" width="280px" alt="Profile picture">
                    </div>
                </div>
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>Publications</h4>
                        {pub}
                    </div>
                </div>
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>Teaching</h4>
                        {teaching}
                    </div>
                </div>
                <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                    {footer}
                </div>
            </div>
        </div?
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')
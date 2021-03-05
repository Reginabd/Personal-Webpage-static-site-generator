
#!/usr/bin/env python3


# Reads in the top.html



top_html = open('./templates/top.html').read()

bottom_html = open('./templates/bottom.html').read()

middle_html = open('./content/index.html').read()

print('combining HTML')

combined_html = top_html + middle_html + bottom_html

print(combined_html)

open('./docs/index.html', 'w+').write(combined_html)



# Reads in the top.html


top_html = open('./templates/top.html').read()


bottom_html = open('./templates/bottom.html').read()


middle_html = open("./content/about.html").read()

print('combining HTML')

combined_html = top_html + middle_html + bottom_html

print(combined_html)

open('./docs/about.html', 'w+').write(combined_html)


# Reads in the top.html

top_html = open('./templates/top.html').read()


bottom_html = open('./templates/bottom.html').read()


middle_html = open('./content/education.html').read()

print('combining HTML')

combined_html = top_html + middle_html + bottom_html

print(combined_html)

open('./docs/content.html', 'w+').write(combined_html)



# Reads in the top.html

top_html = open('./templates/top.html').read()


bottom_html = open('./templates/bottom.html').read()


middle_html = open('./content/experience.html').read()

print('combining HTML')

combined_html = top_html + middle_html + bottom_html

print(combined_html)

open('./docs/experience.html', 'w+').write(combined_html)


# Reads in the top.html

top_html = open('./templates/top.html').read()


bottom_html = open('./templates/bottom.html').read()


middle_html = open('./content/skills.html').read()

print('combining HTML')

combined_html = top_html + middle_html + bottom_html

print(combined_html)

open('./docs/skills.html', 'w+').write(combined_html)

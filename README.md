Nebraska schools news application
=================================
A Django application to display state-level testing data for Nebraska schools. 
Run `pip install -r requirements.txt` to install the dependencies:
- [csvkit](https://csvkit.readthedocs.org/en/0.9.1/)  
- [fabric](http://www.fabfile.org/)

##Overview

Information is gathered from the Nebraska Department of Education [here](http://reportcard.education.ne.gov/pg_DataDownload.aspx?AgencyID=00-0000-000)

The files we use are:
<ul>
<li>Agencies</li>
<li>ACT data </li>
<li> Cohort Graduation data </li>
<li> Dropout Rate data </li>
<li> Federal Accountability Data </li>
<li> Free and Reduced Price Lunch Data </li>
<li> NeSA Math Assessment Data </li>
<li> NeSA Reading Assessment Data </li>
<li> NeSA Science Assessment Data </li>
<li> NeSA Writing Assessment Data </li>
</ul>

The information included in these .txt files aren't all included. We used fabric to parse out the necessary fields, which match up to the models.

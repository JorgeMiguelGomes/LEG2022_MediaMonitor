

# Legislativas2022 - Media Analysis

<span class="c2">How do media outlets' Facebook pages,  cover the main candidates to the Portuguese 2022 legislative elections</span>



# <span class="c24">KEY POINTS</span>

*   <span class="c22 c18">António Costa leads on all quantitative analysis</span>
*   <span class="c22 c18">There is a visible trend that shows that the least seats you have in parliament, the less media exposure you have</span>
*   <span class="c22 c18">There are two outliers to this trend: André Ventura and Rui Tavares</span>

*   <span class="c18 c22">André Ventura due to his political views and the fact the media seem to believe that covering the candidate brings more clicks, that generate more ad revenue</span>
*   <span class="c22 c18">Rui Tavares exposure probably has to do with the novelty factor and what is considered a good performance during the televised debates</span>

*   <span class="c22 c18">When comparing extreme reactions (“Love” and “Angry”) Francisco Rodrigues dos Santos is the surprise, being the candidate that gets more “Love Reactions”</span>
*   <span class="c18">António Costa comes second, only followed by Inês de Sousa Real, in the list of</span> <span class="c18">candidates</span><span class="c22 c18"> that get more “Angry” reactions</span>
*   <span class="c22 c18">André Ventura has a balanced proportion of “Love” and “Angry” reactions which comes as a surprise</span>
*   <span class="c22 c18">The limitation of the keyword dataset to the candidates’ name, and its variations, are an obstacle to this study.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

# <span class="c24">INTRODUCTION</span>

<span class="c36 c38">This document is the result of a more structured approach to an initial analysis done with data from</span> <span class="c68 c36">CrowdTangle</span> <span class="c16">and that was posted on twitter as a food for thought content.</span>

<span class="c16">From that first analysis two charts were created.</span>

<span class="c16">With the provocative title “Who is more mentioned by the media?”, the first chart summed the references to each candidate name, in a period of 7 days, on Facebook posts in 24 Portuguese media outlets</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 302.67px;">![](images/image7.png)</span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c16"></span>

<span class="c38 c36">The second chart aggregated mentions by media outlets, resulting in very interesting results, with the National News Agency taking the spotlight due to its non-diversity.</span> <span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 286.67px;">![](images/image21.png)</span>

<span class="c38 c36">The feedback that the original tweet got</span><sup class="c38 c36">[[1]](#ftnt1)</sup><span class="c16">, including some ideas, confirmed how important this theme is, in a time of general elections, and a decision was made to make a more in depth analysis of the data, by generating new datasets.</span>

<span class="c38 c36">The colors used for each candidate, on the original graphics above, is the official color for each party, except for “António Costa”, where the color used was the old pink color used on the “Partido Socialista” logo. However, and based on the feedback received, the colors used for “Francisco Rodrigues dos Santos” and “Jerónimo de Sousa” are too similar and therefore the color for “Jerónimo dos Santos” will be changed to a different color.</span>

# <span class="c24">OBJECTIVE</span>

<span class="c16">Monitor, quantitatively, how many times media outlets in Portugal mention each candidate, in their titles posted to social media,  during the pre-electoral and electoral campaign for the 2022 elections.</span>

<span class="c38 c36">The definition of  “Candidate” is</span> <span class="c68 c36">the party leader of each party that is running for legislative elections,and whose party got to elect any candidates in the last elections</span><span class="c16">, mirroring the law that states that these parties should be included in televised debates.</span>

<span class="c16"></span>

<span class="c2"></span>

# <span class="c24">MEDIA OUTLETS</span>

<span class="c44 c36">To the original list of 24 media outlets 4 more were added, for a t</span><span class="c18 c36">otal of 28 media outlets being analysed</span><span class="c44 c36">. Media outlets in</span> <span class="c18 c36 c60">bold</span><span class="c8"> are those that were added after the first preliminary analysis</span>

<a id="t.04064802ac6748af79e59fedc88a100877a30b6d"></a><a id="t.0"></a>

<table class="c25">

<tbody>

<tr class="c31">

<td class="c45" colspan="1" rowspan="1">

<span class="c8">Agência Lusa</span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c8">CMTV</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8">CNN Portugal</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8">Correio da Manhã</span>

</td>

</tr>

<tr class="c31">

<td class="c45" colspan="1" rowspan="1">

<span class="c8">Diário de Notícias</span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c8">ECO</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8">EXPRESSO</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c20 c18">ionline</span>

</td>

</tr>

<tr class="c31">

<td class="c45" colspan="1" rowspan="1">

<span class="c8">Jornal de Negócios</span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c8">Jornal de Notícias</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8">Jornal Económico</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c18 c20">Notícias ao Minuto</span>

</td>

</tr>

<tr class="c31">

<td class="c45" colspan="1" rowspan="1">

<span class="c20 c18">NOVO Semanário</span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c8">Observador</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8">Público</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8">Rádio Observador</span>

</td>

</tr>

<tr class="c31">

<td class="c45" colspan="1" rowspan="1">

<span class="c8">Revista Visão</span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c8">RTP</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8">RTP Notícias</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8">RTP1</span>

</td>

</tr>

<tr class="c31">

<td class="c45" colspan="1" rowspan="1">

<span class="c8">SÁBADO</span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c20 c18">SAPO</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c44 c36">SIC</span><sup class="c44 c36">[[2]](#ftnt2)</sup>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c44 c36">SIC Notícias</span><sup class="c36 c44">[[3]](#ftnt3)</sup>

</td>

</tr>

<tr class="c31">

<td class="c45" colspan="1" rowspan="1">

<span class="c8">TSF - Rádio Notícias</span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c8">TVI</span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8"></span>

</td>

<td class="c15" colspan="1" rowspan="1">

<span class="c8"></span>

</td>

</tr>

</tbody>

</table>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c8"></span>

<span class="c24"></span>

<span class="c24"></span>


<span class="c8">At the date of the data extraction, this was the follower count for each media outlet’s page on Facebook</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 282.67px;">![](images/image6.png)</span>

<span>“Jornal de Notícias” and “TVI” are the only media outlets with more than 2M followers on Facebook. In the case of “Jornal de Notícias” this contrasts with the fact that the newspaper doesn’t even make it to the TOP 10 of paid newspapers in Portugal</span><sup>[[4]](#ftnt4)</sup>

<span class="c2">Also of note is the fact that the national news agency “Agência Lusa” and the national TV stations ( RTP, RTP1 and RTP Notícias) do not have many followers on Facebook.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

# <span class="c24">SETTINGS & KEYWORDS</span>

<span class="c37 c36 c39">The keywords used in this study refer only to the candidate, and exclude the party name.</span>

<span class="c36 c68">In order to trim down the dataset to be extracted the search refers only to Pages, with relevance in Portugal, and with the primary admin from Portugal.</span><span class="c37 c36 c61"> </span>

<span class="c6">António Costa</span>

<span class="c2">"António Costa", "Costa", "Líder do PS", "Líder Socialista"</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 134.67px;">![](images/image28.png)</span>

<span class="c37 c18 c41 c71"></span>

<span class="c6">Rui Rio</span>

<span class="c2">"Rui Rio", "Rio", "Líder do PSD", "Líder do PPD/PSD", "Líder da oposição"</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 134.67px;">![](images/image10.png)</span>

<span class="c14"></span>

<span class="c14"></span>

<span class="c14"></span>

<span class="c14"></span>

<span class="c14"></span>

<span class="c14"></span>

<span class="c6"></span>

<span class="c6"></span>

<span class="c6"></span>

<span class="c6">Catarina Martins</span>

<span class="c2">“Catarina Martins”, “Catarina”, “Líder do Bloco”</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 134.67px;">![](images/image12.png)</span>

<span class="c6">Jerónimo de Sousa</span>

<span class="c2">“Jerónimo de Sousa”, “Jerónimo”,”Líder Comunista”</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 134.67px;">![](images/image14.png)</span>

<span class="c6">Francisco Rodrigues dos Santos</span>

<span>"Francisco Rodrigues dos Santos","Líder do CDS" NOT "José Rodrigues dos Santos</span><sup>[[5]](#ftnt5)</sup><span class="c2">"</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 134.67px;">![](images/image20.png)</span>

<span class="c6"></span>

<span class="c6"></span>

<span class="c6">Inês de Sousa Real</span>

<span class="c2">"Inês Sousa Real", "Inês de Sousa Real", "Líder do PAN", "Líder do Partido PAN", “Sousa Real”, “Inês Sousa-Real”</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 124.00px;">![](images/image3.png)</span>

<span class="c6">André Ventura</span>

<span class="c2">"André Ventura", "Ventura", "Líder do CHEGA"</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 124.00px;">![](images/image16.png)</span>

<span class="c6">João Cotrim Figueiredo</span>

<span class="c2">“João Cotrim Figueiredo”, “João Cotrim”, “Cotrim Figueiredo”,“Líder da IL”, “Líder da Iniciativa Liberal”</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 120.00px;">![](images/image26.png)</span>

<span class="c6"></span>

<span class="c6"></span>

<span class="c6"></span>

# <span class="c24"></span>

<span class="c6">Rui Tavares</span>

<span class="c8">“Rui Tavares”, “Líder do LIVRE”, “Líder do Partido Livre”</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 120.00px;">![](images/image17.png)</span>

<span class="c2"></span>

# <span class="c24">METHODOLOGY</span>

1.  <span class="c8">Search Crowdtangle for every candidate’s respective keywords</span>
2.  <span class="c8">Export to .csv</span>
3.  <span class="c8">Import each individual .csv to separate sheets on Google Sheets and rename the sheets with the candidate’s initials</span>
4.  <span class="c44 c36">On a sheet name</span> <span class="c18 c36">“counters”</span><span class="c44 c36">apply the following formula for each candidate</span> <span class="c38 c64">=COUNTIF(candidate_initials!$A$2:$A$9000,</span><span class="c38 c48">media_outlet_name</span><span class="c28">)</span>
5.  <span class="c28">Sum the values on each column</span>
6.  <span class="c28">Generate graphics</span>

<span class="c28"></span>

<span class="c28"></span>

<span class="c10 c37 c41"></span>

<span class="c10 c37 c41"></span>

<span class="c10 c37 c41"></span>

<span class="c10 c37 c41"></span>

<span class="c10 c37 c41"></span>

<span class="c8">The “counters” spreadsheet looks like this</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 376.00px;">![](images/image23.png)</span>

<span class="c44 c36">The resulting numbers are from datasets used in the preliminary analysis, and are</span> <span class="c14">for reference only.</span>

<span class="c8"></span>

# <span class="c24">OBSTACLES</span>

<span>The initial idea was to include in the search the name of the parties. However this idea was dropped given the need for a data treatment and validation process that would rule impossible to make this analysis in a timely manner.</span> <span class="c22 c18">Therefore it was assumed that only the name of the candidates, and consequently the most common variations of the name, was to be used.</span>

<span class="c22 c18"></span>

# <span class="c24"></span>

# <span class="c24">DATASETS</span>

## <span class="c11">General</span>

<span class="c2">The raw dataset exported by CrowdTangle includes the following columns</span>

<span class="c2"></span>

<a id="t.8c3a099e7011dfd8b75eb1d9090c07c4bc7df2b5"></a><a id="t.1"></a>

<table class="c25">

<tbody>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">User Name</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Facebook ID</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Page Category</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Page Admin Top Country</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Page Description</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Page Created</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Likes at Posting</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Followers at Posting</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Post Created</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Post Created Date</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Post Created Time</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Type</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Total Interactions</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Likes</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Comments</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Shares</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Love</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Wow</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Haha</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Sad</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Angry</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Care</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Video Share Status</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Is Video Owner?</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Post Views</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Total Views</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Total Views at all Crossposts</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Video Length</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">URL</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Message</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Link</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Final Link</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Image Text</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Link Text</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Description</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Sponsor ID</span>

</td>

</tr>

<tr class="c31">

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Sponsor Name</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Sponsor Category</span>

</td>

<td class="c0" colspan="1" rowspan="1">

<span>Total Interactions</span><sup>[[6]](#ftnt6)</sup>

</td>

<td class="c0" colspan="1" rowspan="1">

<span class="c2">Overperforming Score</span>

</td>

</tr>

</tbody>

</table>

<span class="c2"></span>

<span>With the amount of information given it is possible to perform several analyses, but we always have to keep in mind that “</span><span class="c18">Posts with the most interactions do not equal posts with the most content views or reach</span><span class="c2">” as per Crowdtangle’s advisory.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

# <span class="c24"></span>

## <span class="c11">António Costa</span>

<span class="c2">Dataset extracted resulted in a .csv file with 2.7MB and 2416 rows.</span>

<span>After filtering the dataset by media outlets, the total references amount to 580, which is a</span> <span class="c18">62.5%</span><span>increase from the preliminary</span> <span>analysis</span><span class="c2">, meaning that the insertion of new keywords and media outlets give us a more precise idea of the amount of coverage this candidate got.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image24.png)</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

# <span class="c24"></span>

## <span class="c11">Rui Rio</span>

<span class="c2">Dataset extracted resulted in a .csv file with 1.3MB and 1143 rows.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image35.png)</span>

<span>After filtering the dataset by media outlets, the total references amount to 341, which is a</span> <span class="c18">53.4%</span><span class="c2"> increase from the preliminary analysis.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">Rui Rio</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image15.png)</span>

<span class="c2">Being Rui Rio the leader of the biggest opposition party, in the last legislature, a direct comparison with the current prime minister shows us that, in all media outlets, there are more references to “António Costa” than to “Rui Rio”, even if we are in a pre-campaign period with both party leaders appearing on TV debates almost daily.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">Catarina Martins</span>

<span class="c2">Dataset extracted resulted in a .csv file with 1MB and 946 rows.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image22.png)</span>

<span>After filtering the dataset by media outlets, the total references amount to 213, which is a</span> <span class="c18">40.8%</span><span class="c2"> increase from the preliminary analysis.</span>

<span>This dataset, that focus on the leader of the third major political force in Portugal, shows the first 0 results with some media outlets not mentioning “Catarina Martins”</span><sup>[[7]](#ftnt7)</sup><span class="c2"> at all during the period in analysis, despite the on-going pre-electoral debates.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c8"></span>

## <span>Jerónimo de Sousa</span><sup>[[8]](#ftnt8)</sup>

<span class="c2">Dataset extracted resulted in a .csv file with 313kb and 254 rows.</span>

<span class="c2"></span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image19.png)</span>

<span>After filtering the dataset by media outlets, the total references amount to 90, which is a</span> <span class="c18">47.8%</span><span class="c2"> increase from the preliminary analysis.</span>

<span>Jerónimo de Sousa is the leader of the 4th biggest party in parliament, during the previous legislature but the data shows that he wasn’t mentioned by 5 of the 28 media outlets (</span><span class="c18">17%</span><span class="c2">) that are under analysis.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">Francisco Rodrigues dos Santos</span>

<span class="c2">Dataset extracted resulted in a .csv file with 118kb and 120 rows.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image32.png)</span>

<span>After filtering the dataset by media outlets, the total references amount to 87, which is a</span> <span class="c18">77.0%</span><span class="c2"> increase from the preliminary analysis. This increase is directly linked to the keywords used for this search. Also noteworthy is the weight of “Observador” in these results, which contributes with more than a quarter of the mentions (27.0%).</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">Inês de Sousa Real</span>

<span class="c2">Dataset extracted resulted in a .csv file with 110kb and 85 rows.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image4.png)</span>

<span>After filtering the dataset by media outlets, the total references amount to 35, which is a</span> <span class="c18">2.07%</span><span class="c2"> decrease from the preliminary analysis, or one mention. This is due to using a  more tight set of keywords for this query.</span>

<span>The lack of representation of PAN’s (Pessoas Animais Natureza) leader in the media outlets is visible, with only 12 media outlets out of 28 (</span><span class="c18">42.9%</span><span class="c2">) mentioning her name, even with the pre-electoral campaign televised debates happening.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">André Ventura</span>

<span class="c2">Dataset extracted resulted in a .csv file with 908kb and 813 rows.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image18.png)</span>

<span>After filtering the dataset by media outlets, the total references amount to 283, which is a</span> <span class="c18">50.2%</span><span class="c2"> increase from the preliminary analysis.</span>

<span>However this dataset deserves more attention because the trend, up to now, was</span> <span class="c18">the less seats you have in parliament the less mentions you have in the media</span><span class="c2">.</span>

<span class="c2">André Ventura (the leader of an extreme-right party) breaks this trend and has more mentions than Catarina Martins, the third biggest political party, in the previous legislature, in Portugal. André Ventura was only able to elect one person, himself, in the last general elections.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">André Ventura</span>

<span class="c2">Repeating the exercise we did before between António Costa and Rui Rio, it’s clear that Ventura has an unproportional media exposure when compared with parties that have much more representation in the parliament.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 329.33px;">![](images/image11.png)</span><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 520.50px; height: 321.14px;">![](images/image2.png)</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">João Cotrim Figueiredo</span>

<span class="c2">Dataset extracted resulted in a .csv file with 127kb and 103 rows.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image13.png)</span>

<span>After filtering the dataset by media outlets, the total references amount to 48, which is a</span> <span class="c18">29.2%</span><span class="c2"> increase from the preliminary analysis.</span>

<span>When the first analysis was published on Twitter, some readers made reference to the fact that it was impossible for “ECO” to not mention “João Cotrim Figueiredo”. After all, the candidate is a columnist in that media outlet and the “ECO” is seen as a supporter of the ideas forwarded by “Iniciativa Liberal”</span><sup>[[9]](#ftnt9)</sup><span class="c2">.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">João Cotrim Figueiredo</span>

<span class="c2">However a quick search on ECO’s website shows us the reason why this happens</span><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 542.50px; height: 400.37px;">![](images/image8.png)</span>

<span class="c2"></span>

<span class="c2">The title references are never done using the candidate’s name, but the party name or “Liberais” (meaning those that belong to the party “Iniciativa Liberal”)</span>

<span class="c22 c18">This is an important insight that can lead to changes in the way candidates are referred to in the titles that are shared on Facebook / Social Media channels.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span>Rui Tavares</span>

<span class="c2">Dataset extracted resulted in a .csv file with 263kb and 226 rows.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 385.33px;">![](images/image1.png)</span>

<span>After filtering the dataset by media outlets, the total references amount to 96, which is a</span> <span class="c18">30.2%</span><span class="c2"> increase from the preliminary analysis.</span>

<span>The effect of the televised debates, and pre-electoral campaign, can be clearly observed here. Rui Tavares’s party, “Livre” did elect one candidate in the previous electoral elections, but that candidate cut its ties to the party</span><sup>[[10]](#ftnt10)</sup><span class="c2">.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

# <span class="c24">ANALYSIS</span>

<span class="c2">We will start by plotting the same two original graphs, based on the values retrieved from the new datasets.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 253.33px;">![](images/image29.png "Who gets more mentions in the media?")</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 269.33px;">![](images/image36.png "Who is more mentioned by media outlet")</span>

<span class="c2"></span>

<span>The observed trend on the preliminary analysis doesn’t change: Mentions by number of seats in Parliament decrease in line with what is expected, and “André Ventura” is the exceptio along with  “Rui Tavares” that also has a number of mentions that</span> <span>doesn’t</span><span class="c2"> reflect the party’s representation in parliament, probably due to the participation in televised debates,a good performance at those, and for  being the novelty candidate.</span>

<span class="c2">Performing a standardization of the data, this is the overall picture of the combined datasets.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 346.67px;">![](images/image27.png "Main Dataset: Normalized Data - Overview")</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

# <span class="c24">FURTHER ANALYSIS</span>

<span>However it is important to dig further into the data available and understand how these mentions correlate with some of the metrics present in the dataset, particularly “Shares”, “Likes”, “Love” and “Angry” in an attempt to have a very basic, but yet important,</span> <span class="c29">sentiment</span><span class="c2"> analysis of the content.</span>

<span class="c2">Why are “Love” and “Angry” reactions important?</span>

<span>“</span><span class="c26">Five years ago, Facebook gave its users five new ways to react to a post in their news feed beyond the iconic “like” thumbs-up: “love,” “haha,” “wow,” “sad” and “angry.”</span>

<span class="c29 c30">Behind the scenes, Facebook programmed the algorithm that decides what people see in their news feeds to use the reaction emoji as signals to push more emotional and provocative content — including content likely to make them angry. Starting in 2017,</span> <span class="c29 c62">Facebook’s ranking algorithm treated emoji reactions as five times more valuable than “likes,”</span> <span class="c30 c29">internal documents reveal. The theory was simple: Posts that prompted lots of reaction emoji tended to keep users more engaged, and keeping users engaged was the key to Facebook’s business.</span><span class="c30">”</span><sup class="c30">[[11]](#ftnt11)</sup>

<span class="c2"></span>

<span class="c2">In the next pages that analysis will be done, using the data provided by CrowdTangle.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">Shares</span>

<span class="c2">“Shares”, per candidate, were calculated based on the datasets. “Catarina Martins”, with less mentions, amasses more shares, on Facebook, than Rui Rio. However both combined don’t surpass “André Ventura” in the number of shares.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 402.67px;">![](images/image5.png "Total shares by candidate")</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">Shares</span>

<span>When analyzing the shares by media outlets, it’s clear the prevalence of “António Costa” in all media outlets, except on “Rádio Observador”. However we are talking about</span> <span class="c18">65</span><span> mentions, with no other candidate mention being shared by those that follow “Rádio Observador”. Also keep in mind that this page only has 1708 followers</span><sup>[[12]](#ftnt12)</sup><span class="c2">.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 330.67px;">![](images/image33.png "Shares by media outlet")</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">Likes</span>

<span>As with “Shares” the total of likes, per candidate, were calculated based on the datasets. “Catarina Martins”, with less mentions, amasses more likes, marginally, on Facebook than Rui Rio. However both combined don’t surpass “André Ventura” in the number of likes.</span> <span class="c18">This is consistent with the trend observed with</span> <span class="c18">shares</span><sup>[[a]](#cmnt1)</sup><span class="c22 c18">.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 329.33px;">![](images/image30.png "Total Likes by candidate")</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span>When exploring the amount of likes, per media outlet, that each candidate’s mention gets, it’s important to note the performance of “António Costa” that even in media outlets where he gets less mentions, gets a majority of likes, as observed in “SIC”</span> <span class="c18">where with only 30% of mentions gets 89.7% of likes</span><span class="c2">.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 402.67px;">![](images/image5.png "Total shares by candidate")</span><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 401.33px;">![](images/image31.png "Likes by media outlet")</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">LOVE vs ANGRY</span>

<span class="c2">Facebook provides users with a set of reactions. “Love” and “Angry” are the extremes and can be used to extract a basic sentiment analysis of the content. These reactions, as explained before, have more weight than the regular “Likes”</span>

<span class="c2">When comparing the amount of “Love” and “Angry” reactions that each candidate got, during the period in analysis, the results go against common sense.</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 340.00px;">![](images/image25.png "Love vs Angry Comparison ")</span>

<span>“António Costa” (</span><span class="c18 c51">68.2%</span><span>) is only second in “Angry” reactions to “Inês Sousa Real”(</span><span class="c18 c51">76.9%</span><span>), and “Francisco Rodrigues dos Santos” is the mention that gets more “Love” (</span><span class="c65">61.3%</span><span class="c2">)</span>

<span>Also of note is “André Ventura” (</span><span class="c18 c51">45.7%</span><span class="c2">) that attracts a balanced mix of “Angry” and “Love” reactions when he is mentioned by media outlets on Facebook.</span>

<span class="c2">This results can be indicative of user sentiment, but a much more complex analysis would have to be done in order to determine it properly.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

# <span class="c24">CONCLUSIONS AND NEXT STEPS</span>

## <span class="c11">CONCLUSIONS</span>

<span class="c2">Based on the extracted dataset the media mentions of the several candidates is unbalanced. Some candidates get less mentions than others, even if we are in a period of pre-electoral campaign, with all the candidates participating in televised debates.</span>

<span class="c2">The data gathered raises questions of how organic/natural the behaviour for “André Ventura” is but, nevertheless, it is clear that media outlets mention the candidate in a disproportionate way, when compared with the leader and candidate of the third major party in the parliament , “Catarina Martins”, and with candidates that have the same representation in the parliament that ceases functions now.</span>

## <span class="c11">NEXT STEPS</span>

<span class="c2">The search queries will be run again on January 29th with the results posted on twitter on the same day.</span>

<span class="c2">The period in analysis will be January 01st to January 28th</span>

<span class="c2">A report will be written afterwards, already taking into account the election’s results.</span>

<span class="c2"></span>

## <span class="c11">ACKNOWLEDGEMENTS</span>

<span class="c2">James Morgan, META</span>

<span class="c2">João Pires Ribeiro, IST</span>

<span class="c2">João Oliveira, Independent Communications Consultant</span>

<span class="c2">Miguel Paisana, Obercom</span>

<span class="c2">Inês Narciso, ISCTE</span>

<span class="c2">Isabel Silva, everything</span>

<span class="c2"></span>

<span class="c2"></span>

## <span class="c11">ABOUT CROWDTANGLE</span>

<span class="c2">All data in this report comes from CrowdTangle, a Facebook-owned tool that tracks interactions on public content from Facebook pages and groups, verified profiles, Instagram accounts, and subreddits. It does not include paid ads unless those ads began as organic, non-paid posts that were subsequently “boosted” using Facebook’s advertising tools. It also does not include activity on private accounts, or posts made visible only to specific groups of followers.</span>

<span class="c2">CrowdTangle is a public insights tool from Facebook that makes it easy to follow, analyze, and report on what’s happening across social media. Facebook acquired CrowdTangle in November, 2016, made the tool free, and expanded access from 300 media partners to more than 10,000, including global sports leagues, local newspapers, digital publishers, music labels, celebrity accounts, and more.</span>

<span class="c2">Starting in 2019, CrowdTangle added research, academic and fact-checking partners, and built tools to help these partners study how public content spreads across Facebook and Instagram. By building products to more easily track public content, CrowdTangle has become the best way for outside organizations to have greater transparency into what’s happening on Facebook and Instagram. The hope is that a greater shared understanding around how public content spreads will shape the broader online conversation, and help make information on social media safer, more reliable, and more accurate.</span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

<span class="c2"></span>

# <span class="c24">LICENSE</span>

<span class="c2"></span>

<span class="c2">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License</span>

<span>By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.</span>

<span class="c37 c59"></span>

<div>

[![License](https://upload.wikimedia.org/wikipedia/commons/f/f1/Cc-by-nc-nd_icon.svg)]

</div>

* * *

<div>

[[1]](#ftnt_ref1)<span class="c40"> </span><span class="c35"> [The tweet](https://twitter.com/JGomes_PT/status/1480208101378822144)<span class="c35">had</span> <span class="c35 c67">43490</span><span class="c9"> impressions on January 10th 2022\.</span>

</div>

<div>

[[2]](#ftnt_ref2)<span class="c33"> The media group that owns SIC was a victim of a ransomware attack during this period.The values shown do not reflect the channel’s communication in a normal period.</span>

</div>

<div>

[[3]](#ftnt_ref3)<span class="c33"> The media group that owns SIC Notícias was a victim of a ransomware attack during this period.The values shown do not reflect the channel’s communication in a normal period.</span>

</div>

<div>

[[4]](#ftnt_ref4)<span class="c40">[PT]</span><span class="c27">[Cision Report](https://www.cision.pt/2021/09/imprensa-circulacao-paga-cresce-face-a-2020/)</span><span class="c33"> </span>

</div>

<div>

[[5]](#ftnt_ref5)<span class="c9"> José Rodrigues dos Santos, who shares the same family names with the candidate, is a Portuguese journalist and book author. The search settings take that into account and ignore any results where “José Rodrigues dos Santos” appears.</span>

</div>

<div>

[[6]](#ftnt_ref6)<span class="c40"> </span><span class="c43"> **weighted**  —  Likes 1x Shares 1x Comments 1x Love 1x Wow 1x Haha 1x Sad 1x Angry 1x Care 1x</span>

</div>

<div>

[[7]](#ftnt_ref7)<span class="c33"> Please refer to Settings and Keywords for all the keywords used in the search</span>

</div>

<div>

[[8]](#ftnt_ref8)<span class="c33"> Although the official color of PCP (Portuguese Communist Party) is red, and the color of the coalition between PCP and the Portuguese Green party is blue, a decision was made to use yellow as the color for Jerónimo de Sousa, as both official colors don’t have enough contrast when joined with the other parties. The yellow chosen is the one from the [flag of the former Soviet Union](https://en.wikipedia.org/wiki/Flag_of_the_Soviet_Union)</span>

</div>

<div>

[[9]](#ftnt_ref9)<span class="c33">** This is an opinion **</span>

</div>

<div>

[[10]](#ftnt_ref10)<span class="c33"> [Joacine deixa de representar Livre](https://www.publico.pt/2020/02/03/politica/noticia/joacine-deixa-representar-livre-passa-deputada-naoinscrita-partir-hoje-1902643)</span>

</div>

<div>

[[11]](#ftnt_ref11)<span class="c40"> </span><span class="c27"> [Washington Post - Five points for anger, one for a ‘like’: How Facebook’s formula fostered rage and misinformation](https://www.washingtonpost.com/technology/2021/10/26/facebook-angry-emoji-algorithm/)</span><span class="c33"> / **Emphasis by the author**</span>

</div>

<div>

[[12]](#ftnt_ref12)<span class="c40"> At the time the data was extracted. Please refer to page</span> <span class="c18 c40">26</span><span class="c33"> for normalized analysis</span>

</div>

<div>

[[13]](#ftnt_ref13)<span class="c33">[ Full terms of this License can be found here](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode)</span>

</div>


select date, classification, title,
       concat('http://history-lab.org/documents/', id) id
from declassification_frus.docs
where body like '%pandemic%' or
      body like '%epidemic%' or
      body like '%ebola%' or
      body like '%hepatitis%' or
      body like '%dengue fever%' or
      body like '%meningitis%' or
      body like '%polio%' or
      body like '%encephalitis%' or
      body like '%malaria%' or
      body like '%measles%' or
      body like '%smallpox%' or
      body like '%typhus%' or
      body like '%yellow fever%' or
      body like '%cholera%' or
      body like '%bubonic plague%' or
      body like '%1918 flu%' or
      body like '%spanish flu%' or
      body like '%hong kong flu%' or
      body like '%asian flu%' or
      body like '%influenza%'
order by date

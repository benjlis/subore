select authored, classification, title, document_uri
from foia2lib_cfpf.marc_records
where title like '%epidemic%' or
      title like '%pandemic%' or
      title like '%ebola%' or
      title like '%hepatitis%' or
      title like '%dengue fever%' or
      title like '%meningitis%' or
      title like '%polio%' or
      title like '%encephalitis%' or
      title like '%malaria%' or
      title like '%measles%' or
      title like '%smallpox%' or
      title like '%typhus%' or
      title like '%yellow fever%' or
      title like '%cholera%' or
      title like '%bubonic plague%' or
      title like '%1918 flu%' or
      title like '%spanish flu%' or
      title like '%hong kong flu%' or
      title like '%asian flu%' or
      title like '%influenza%'
order by authored

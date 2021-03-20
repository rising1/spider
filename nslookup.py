import nslookup as nsl

domain = "bbc.com"

ips_record = nsl.dns_lookup(domain)
print(ips_record.response_full, ips_record.answer)

soa_record = nsl.soa_lookup(domain)
print(soa_record.response_full, soa_record.answer)
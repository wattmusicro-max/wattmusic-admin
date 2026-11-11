#!/usr/bin/env python3
"""One-time split of the two Elementor widgets into module files (lossless)."""
import sys, os
SRC = sys.argv[1]
B = {
 'tm0admw': ('src/admin', [(0,'00-baza'),(41820,'10-tm-names'),(42302,'20-social-vz'),(67908,'30-social-snap'),(92421,'40-kpi'),(104183,'50-asociate'),(113284,'51-asociate-ui'),(120730,'60-deal-trupe'),(125889,'52-asociate-sold')]),
 'tm0ofradm': ('src/oferte', [(0,'00-anti-salt'),(252,'01-oferte-baza'),(19124,'02-prefill'),(20847,'03-busy-data'),(22645,'04-libere-whatsapp'),(28539,'05-trupa-mea-acces'),(33479,'06-editare'),(40514,'07-prelungire'),(44391,'08-cautare'),(46979,'09-intalniri'),(53973,'10-intalniri-panou'),(56818,'11-disponibilitate'),(64281,'12-pipeline'),(77712,'13-statistici'),(94091,'14-verificare-data'),(95509,'15-verificare-locatie'),(97273,'16-descalificati'),(104372,'17-calendar-leaduri'),(120906,'18-contracte-semnate'),(128999,'19-whatsapp-web'),(129824,'20-backup-zilnic')]),
}
for wid,(d,parts) in B.items():
    h = open(os.path.join(SRC, wid + '.html'), encoding='utf-8', newline='').read()
    order = []
    for i,(start,name) in enumerate(parts):
        end = parts[i+1][0] if i+1 < len(parts) else len(h)
        fn = name + '.html'
        open(os.path.join(d, fn), 'w', encoding='utf-8', newline='').write(h[start:end])
        order.append(fn)
    open(os.path.join(d, 'ORDINE.txt'), 'w').write('\n'.join(order) + '\n')

# International Rugby ELO ranking & Investec Cup

We use about 400 head to head games to calculate the ELO rating for the top 15
rugby nations in the world.

- data.py: get match data from rugbypass
- utils.py: some ELO functions
- calc_rating.py: use the match data to calculate ELO
- calc_rating_investec.py: use the match data to calculate ELO for Investec Cup (clubs)

I have updated the ELO function a bit to take into account the match score.

Note that the point difference is distributed as $N(5, 21.5^2)$

The ELO ranking is very similar to the [official ranking](https://www.world.rugby/tournaments/rankings/mru)

## Ranking 

542.8 South Africa
488.3 New Zealand
451.1 France
441.3 Ireland
413.5 Samoa
412.3 Argentina
399.9 England
380.6 Scotland
367.2 Fiji
362.4 Georgia
362.3 Australia
353.9 Wales
347.3 Tonga
342.7 Japan
334.4 Italy

Last updated: Nov 2025

## Investec ranking

(507.82225904383023, 'Toulouse')
(492.5070181519389, 'Leinster')
(490.0828582844572, 'Bordeaux')
(475.86512197478555, 'Northampton')
(421.16476949020034, 'Castres')
(417.27988260562864, 'Harlequins')
(402.3458055220044, 'Stormers')
(401.1144929189108, 'Bayonne')
(399.4722478417764, 'Bulls')
(392.32633837224716, 'Glasgow')
(392.260591865061, 'Clermont')
(392.0298221526318, 'Rochelle')
(390.62972141630223, 'Bath')
(390.45978202135103, 'Benetton')
(390.01741764269366, 'Lyon')
(387.83105998400464, 'Toulon')
(383.2910597529287, 'Sharks')
(381.14907129541183, 'Connacht')
(380.108027555811, 'Saracens')
(379.98813504429313, 'Exeter')
(379.0108163058288, 'Munster')
(376.00400344259936, 'Sale')
(375.87201984507846, 'Racing')
(368.12494939153885, 'Leicester')
(364.33817543316053, 'Bristol')
(361.1334211249548, 'Cardiff')
(359.0442930240105, 'Ulster')
(348.72683849655994, 'Paris')

Last updated: Nov 2025


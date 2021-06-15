# Display net worth over time, grouped by account type, with a linear fit

require(ggplot2)

df <- read.csv('bones.csv', colClasses=c('Date', NA, 'integer'))

pt <-
	ggplot(df, aes(x=ts, y=keys, color=cat, fill=cat)) +
	geom_line() +
	scale_y_continuous(breaks=seq(0, 160, 10)) +
	scale_x_date(
		date_breaks='6 months',
		limits=c(as.Date('2020-05-01'), as.Date('2023-05-01'))
	) +
	stat_smooth(method='glm', linetype=3, fullrange=TRUE) +
	theme_bw()

ggsave('bones.svg', plot=pt, width=24, height=12, units='cm')

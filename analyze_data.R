library(ggplot2)
df = read.csv("data.csv",header=F,col.names = c("packet_size","ping_time"))

lin_regr = lm(ping_time ~ packet_size, data=df)
lbl = paste("linear regression: ping =",signif(summary(lin_regr)$coef[[1]],digits = 3),
            "+",signif(summary(lin_regr)$coef[[2]],digits = 3),
            "* size","; r2 =",signif(summary(lin_regr)$r.squared,digits = 3))

png(file='ping_analysis_graph.png',width=800,height=600)

ggplot(data = df, aes(x = packet_size, y = ping_time)) +
  geom_point(aes(colour=packet_size)) +
  stat_smooth(method = "lm", color="red") +
  ggtitle(label=lbl)

dev.off()
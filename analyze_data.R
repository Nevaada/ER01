# Getting the data

df = read.csv("data.csv",header=F,col.names = c("packet_size","ping_time"))

# Creating the .png file

png(file='ping_analysis_graph.png',width=800,height=600)
plot(ping_time~packet_size,data=df,main="Ping Analysis Graph")
coeff_lm = lm(ping_time~packet_size,data=df)
abline(coeff_lm,col="blue")
dev.off()

summary(coeff_lm)


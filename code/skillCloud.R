# First Set the working directory as below
# Eg setwd("/home/arul/workspace/website/code")
skillsFile <- "../data/skills.txt"

skills <- read.table(skillsFile,header=TRUE)

# Adjustments done are as follows
# 1. Modifying values uniformly to generate a neat graph
# 2. JavaEnterpriseEdition is too long for the library (reducing it to J2EE)
skills[,2] <- skills[,2]*10+5

png(filename="../templates/portfolio/images/skills_wc_1.png",width=12,height=8, units='in', res=300)
    #width=1500, height=1500)
wordcloud(skills$Skills,skills$Endorsements,random.order=FALSE,
          random.color= TRUE,colors=brewer.pal(8, "Dark2"))

dev.off()

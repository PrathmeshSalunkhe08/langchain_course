from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq

import sys
load_dotenv()

sys.stdout.reconfigure(encoding='utf-8')

LLM = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3,
    max_tokens=500
)

text="""
# Bhagat Singh – The Revolutionary Freedom Fighter

Bhagat Singh was one of the most influential revolutionaries of the Indian independence movement. He is remembered for his courage, patriotism, revolutionary ideas, and willingness to sacrifice his life for the freedom of India. Although he lived for only 23 years, his thoughts and actions had a lasting impact on India's struggle against British rule. Even today, Bhagat Singh is remembered as a symbol of courage, sacrifice, and the desire for freedom.

Bhagat Singh was born on 28 September 1907 in Banga village, which was then part of Punjab and is now in Pakistan. He was born into a family that was deeply involved in India's freedom movement. His father, Kishan Singh, and his uncles were associated with the struggle against British rule. Because of his family background, Bhagat Singh developed an interest in India's independence from a very young age.

One incident that strongly influenced Bhagat Singh was the Jallianwala Bagh massacre of 1919. On 13 April 1919, British troops under General Reginald Dyer fired on a large gathering of Indians at Jallianwala Bagh in Amritsar. Hundreds of people were killed and many others were injured. Bhagat Singh was deeply affected by the incident. According to accounts of his life, he visited the site when he was still a young boy. The massacre strengthened his determination to fight against British rule.

Bhagat Singh was also influenced by the Non-Cooperation Movement led by Mahatma Gandhi. He admired the idea of fighting for independence, but after the movement was withdrawn following the Chauri Chaura incident in 1922, he became interested in revolutionary methods and political ideas. As he grew older, he began reading extensively about revolution, socialism, history, economics, and political philosophy.

Bhagat Singh became associated with revolutionary organizations and young activists who wanted to end British colonial rule. He became an important member of the Hindustan Socialist Republican Association (HSRA). The organization aimed to establish an independent India and was influenced by socialist ideas. Bhagat Singh believed that political freedom alone was not enough. He also wanted a society based on equality and justice.

One of the most important events associated with Bhagat Singh was the protest against the Simon Commission. The British government had appointed the Simon Commission in 1927 to discuss constitutional reforms in India, but it did not include any Indian members. Indians across the country protested against the commission.

During one such protest in Lahore in 1928, Lala Lajpat Rai led a demonstration against the Simon Commission. The police used force to disperse the protesters, and Lala Lajpat Rai was seriously injured. He later died from his injuries. Bhagat Singh and his revolutionary colleagues believed that the British police officer responsible for the assault should be punished.

In December 1928, Bhagat Singh and his associates planned to target James A. Scott, whom they held responsible for the police action against Lala Lajpat Rai. However, due to a case of mistaken identity, police officer John Saunders was shot and killed instead. Bhagat Singh and Rajguru then escaped from Lahore.

Another major event occurred on 8 April 1929. Bhagat Singh and Batukeshwar Dutt threw low-intensity bombs in the Central Legislative Assembly in Delhi. Their objective was not to kill people but to protest against repressive legislation and make their political message heard. After throwing the bombs, they deliberately stayed at the scene and allowed themselves to be arrested. They also shouted slogans and distributed revolutionary literature.

During his trial and imprisonment, Bhagat Singh used the courtroom and prison as platforms to express his political ideas. He and his fellow prisoners protested against the poor treatment of Indian political prisoners. They demanded better food, clothing, reading materials, and equal treatment. Bhagat Singh participated in a long hunger strike in prison. Jatin Das, another revolutionary prisoner, died after a prolonged hunger strike.

Bhagat Singh was also a strong supporter of intellectual development. He believed that revolution was not simply about violence or armed struggle. He emphasized the importance of ideas, education, political awareness, and social change. His writings demonstrate his interest in socialism, atheism, nationalism, and political philosophy.

One of his famous writings is "Why I Am an Atheist," in which he explained his views about religion and belief. He argued that people should develop their own understanding through reason and critical thinking. His writings show that he was not merely a young revolutionary carrying out political actions; he was also a serious thinker who spent considerable time reading and reflecting on society and politics.

Bhagat Singh, Rajguru, and Sukhdev were eventually sentenced to death for their involvement in the Saunders case. On 23 March 1931, Bhagat Singh, Rajguru, and Sukhdev were executed in Lahore Jail. Bhagat Singh was only 23 years old.

His death created widespread public emotion across India. Many young Indians were inspired by his courage and sacrifice. Although different political leaders and groups had different approaches to achieving independence, Bhagat Singh became a powerful symbol of resistance to British colonial rule.

It is important to understand Bhagat Singh not only through his image as a revolutionary but also through his ideas. He believed that freedom should involve social and economic justice. He was critical of exploitation and inequality and supported socialist principles. He wanted people to become politically conscious and actively participate in creating a better society.

Bhagat Singh's legacy continues to influence India. His name is associated with bravery, sacrifice, intellectual curiosity, and commitment to a larger cause. Schools, colleges, public institutions, and cultural works across India continue to remember him. His writings are still read by students, historians, and people interested in India's freedom movement.

In conclusion, Bhagat Singh occupies an important place in the history of India's independence struggle. His life was short, but his impact was enormous. From his early exposure to the freedom movement to his revolutionary activities, imprisonment, hunger strike, writings, and final sacrifice, his life reflected his strong commitment to India's independence. His story reminds us that freedom movements are shaped not only by political leaders but also by young people who are willing to question injustice and stand for their beliefs. Bhagat Singh's courage, ideas, and sacrifice have ensured that his name continues to remain an important part of India's history.

"""

summary_template = """
1.Summarize the following text: {text} in few lines .
2.give 2 facts which is intresting
3.dont use any bold formatting.
4.keep the format clean.

"""

prompt = PromptTemplate(
    input_variables=["text"],
    template=summary_template
)
formatted_prompt = prompt.invoke({"text":text})

result=LLM.invoke(formatted_prompt)
print(result.content.replace("**", ""))
    
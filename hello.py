import streamlit as st
import pandas as pd
import time as t
st.image("logo.png")

st.title("Hello its Sapg")
st.subheader("MEANS SAPEKSH GOOGLE")
st.markdown("HERE IS SOME CRICKET RECORD OF BATTING AND BOWLING")

a = pd.read_csv("battingrecord.csv")
st.dataframe(a)

B = pd.read_csv("book 1.csv")
st.dataframe(B)

c = st.selectbox("ENTER YOUR favorite player jersy number",(10,7,18,9,64,6,5,77,11, ))

button = st.button("done")
if c==7:
  st.markdown("The Board of Control for Cricket in India (BCCI) retired the number 7"
              " jersey in honor of MS Dhoni, the former captain who won many trophies during his tenure"
              ", including the ODI and T20 World Cups, Champions Trophy, and the Test Mace. The number 7 jersey"
              " is now reserved for Dhoni, the second Indian to receive this honor, after Sachin Tendulkar."
              ""
              ""
              "Stephen Fleming is a former New Zealand cricketer and current coach. "
              "He played from 1994 to 2008, and is New Zealand's second-most capped "
              "Test cricketer with 111 appearances. Fleming is a left-handed top order"
              " batter and is considered one of New Zealand's best batters and most successful captains."
              " He has coached the Melbourne Stars and the Chennai Super Kings")

elif c==18:
  st.markdown("Virat Kohli, the captain of the Indian cricket team,"
              " wears the number 18 jersey in international matches and for his IPL franchise, "
              "Royal Challengers Bangalore. He has worn the number 18 since his under-19 days "
              "in 2008, when he captained the World Cup-winning under-19 side. The number 18 is also the "
              "jersey number his father, Prem Kohli, used to wear when he played cricket. Kohli "
              "has also said that the number 18 is important to him because his debut for India "
              "was on August 18, 2008, and his father passed away on December 18, 2006")

elif c==9:
    st.markdown("Brian Lara, a former West Indies cricketer, is known for wearing the number 9 jersey."
                " Lara is a left-handed batsman who holds the record for the most runs scored in an"
                " innings in both first-class and Test cricket. He also holds several world records, "
                "including the highest individual score in first-class cricket, the highest individual"
                " score in Test cricket, and the fastest batsman to score 10,000 and 11,000 Test runs.")
elif c==64:
    st.markdown("Cricket Australia retired Phillip Hughes' one-day international shirt number 64 in his"
                " memory. Hughes, a left-handed batsman, was hit on the head by a bouncer during a 2014"
                " Sheffield Shield game and died from his injuries. The scorecard for Hughes' final innings "
                "was amended to show him as 63 not out, rather than retired hurt. In 2015, a tribute match of"
                " 63 overs per team featuring some Australians was held in Nepal, featuring the number 64 "
                "retired.")
elif c==10:
    st.markdown("The Board of Control for Cricket in India (BCCI) retired the number 10 jersey worn by "
                "Sachin Tendulkar in 2017 as a tribute to his career and contributions to the game. The "
                "number 10 jersey is often worn by the team's best batsman or all-rounder, and is considered"
                " one of the most iconic jersey numbers in cricket. Tendulkar is considered an all-time great, "
                "along with Sir Don Bradman and Sir Viv Richards. He started his international cricket career "
                "wearing 99 before switching to 33, and eventually wore the number 10, which sounded like his "
                "surname")
elif c==11:
    st.markdown("Daniel Luca Vettori is a former New Zealand cricketer and current assistant coach for"
                " Australia's men's national cricket team. He was born in Auckland, New Zealand on January"
                " 27, 1979. Vettori is the youngest player to represent New Zealand in Test cricket, with "
                "112 caps. He is also the first cricketer of Italian descent to represent New Zealand. "
                "Vettori bats left-handed and bowls slow left arm orthodox. He has played for the New"
                " Zealand national cricket team, Delhi Daredevils, ICC World XI, and Jamaica Tallawahs.")
elif c==5:
    st.write("Chris Harris is a former New Zealand cricketer who was born on November 20, 1969 in"
             " Christchurch, Canterbury. He is a left-handed batsman and right-arm medium bowler. "
             "Harris is known for his versatility with the bat and slow-medium wobblers. He is "
             "considered one of New Zealand's best fielders and the third highest wicket-taker in"
             " One-Day Internationals (ODIs). Harris is now a medical representative")
elif c==6:
    st.markdown("Nathan Astle is a former New Zealand cricketer who played in all formats of "
                "the game. He was born on September 15, 1971 in Christchurch, Canterbury, New"
                " Zealand. He bats right-handed and bowls right-arm medium")
elif c==77:
    st.markdown("Paras Khadka is a former Nepalese cricketer and the current captain "
                "of the Nepal national team. He was born on October 24, 1987, and is "
                "an all-rounder who bats right-handed and bowls off spin. He captained"
                " the Nepalese cricket team from 2008 to 2019, and is also the current "
                "Secretary of Cricket Association of Nepal and President of Bagmati Province Cricket Association")
else:
    st.markdown("select from select box It is not retiered jersy number")

with st.spinner("just wait"):
      t.sleep(10)

st.balloons()

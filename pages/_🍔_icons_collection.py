# Done by Muench
import streamlit as st


def main():
    st.set_page_config(page_title="icons", page_icon="🍔", layout="wide")

    sysmenu = '''
                  <style>
                  #MainMenu {visibility:hidden;}
                  footer {visibility:hidden;}
                  '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    # Smileys & Emotion
    #   face-smiling
    st.write("😀 😃 😄 😁 😆 😅 🤣 😂 🙂 🙃 🫠 😉 😊 😇")
    #   face-affection
    st.write(" 🥰 😍 🤩 😘 😗 ☺ 😚 😙 🥲")
    #   face-tongue
    st.write("😋 😛 😜 🤪 😝 🤑 ")
    #   face-hand
    st.write("🤗 🤭 🫢 🫣 🤫 🤔 🫡")
    #   face-neutral-skeptical
    st.write("🤐 🤨 😐 😑 😶 🫥 😶 😏 😒 🙄 😬 😮 🤥 🫨")
    #   face-sleepy
    st.write("😌 😔 😪 🤤 😴")
    #   face-unwell
    st.write("😷 🤒 🤕 🤢 🤮 🤧 🥵 🥶 🥴 😵 😵 🤯")
    #   face-hat
    st.write("🤠 🥳 🥸")
    #   face-glasses
    st.write("😎 🤓 🧐")
    #   face-concerned
    st.write("😕 🫤 😟 🙁 ☹ 😮 😯 😲 😳 🥺 🥹 😦 😧 😨 😰 😥 😢 😭 😱 😖 😣 😞 😓 😩 😫 🥱")
    #   face-negative
    st.write("😤 😡 😠 🤬 😈 👿 💀 ☠")
    #   face-costume
    st.write("💩 🤡 👹 👺 👻 👽 👾 🤖")
    #   cat-face
    st.write("😺 😸 😹 😻 😼 😽 🙀 😿 😾")
    #   monkey-face
    st.write("🙈 🙉 🙊")
    #   heart
    st.write("💌 💘 💝 💖 💗 💓 💞 💕 💟 ❣ 💔 ❤ ❤ ❤ 🩷 🧡 💛 💚 💙 🩵 💜 🤎 🖤 🩶 🤍")
    #   emotion
    st.write("💋 💯 💢 💥 💫 💦 💨 🕳 💬 👁 🗨 🗯 💭 💤")
    # People & Body
    #   hand-fingers-open
    st.write("👋 🤚 🖐 ✋ 🖖 🫱 🫲 🫳 🫴 🫷 🫸")
    #   hand-fingers-partial
    st.write("👌 🤌 🤏 ✌ 🤞 🫰 🤟 🤘 🤙")
    #   hand-single-finger
    st.write("👈 👉 👆 🖕 👇 ☝ 🫵")
    #   hand-fingers-closed
    st.write("👍 👎 ✊ 👊 🤛 🤜")
    #   hands
    st.write("👏 🙌 🫶 👐 🤲 🤝 🙏")
    #   hand-prop
    st.write("✍ 💅 🤳")
    #   body-parts
    st.write("💪 🦾 🦿 🦵 🦶 👂 🦻 👃 🧠 🫀 🫁 🦷 🦴 👀 👁 👅 👄 🫦")
    #   person
    st.write("👶 🧒 👦 👧 🧑 👱 👨 🧔 🧔 🧔 👨 👨 👨 👨 👩 👩 🧑 👩 🧑 👩 🧑 👩 🧑 👱 👱 🧓 👴 👵")
    #   person-gesture
    st.write("🙍 🙍 🙍 🙎 🙎 🙎 🙅 🙅 🙅 🙆 🙆 🙆 💁 💁 💁 🙋 🙋 🙋 🧏 🧏 🧏 🙇 🙇 🙇 🤦 🤦 🤦 🤷 🤷 🤷")
    #   person-role
    st.write("🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 👮 👮 👮 🕵 🕵 🕵 💂 💂 💂 🥷 👷 👷 👷 🫅 🤴 👸 👳 👳 👳 👲 🧕 🤵 🤵 🤵 👰 👰 👰 🤰 🫃 🫄 🤱 👩 👨 🧑")
    #   person-fantasy
    st.write("👼 🎅 🤶 🧑 🦸 🦸 🦸 🦹 🦹 🦹 🧙 🧙 🧙 🧚 🧚 🧚 🧛 🧛 🧛 🧜 🧜 🧜 🧝 🧝 🧝 🧞 🧞 🧞 🧟 🧟 🧟 🧌")
    #   person-activity
    st.write("💆 💆 💆 💇 💇 💇 🚶 🚶 🚶 🧍 🧍 🧍 🧎 🧎 🧎 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🏃 🏃 🏃 💃 🕺 🕴 👯 👯 👯 🧖 🧖 🧖 🧗 🧗 🧗")
    #   person-sport
    st.write("🤺 🏇 ⛷ 🏂 🏌 🏌 🏌 🏄 🏄 🏄 🚣 🚣 🚣 🏊 🏊 🏊 ⛹ ⛹ ⛹ 🏋 🏋 🏋 🚴 🚴 🚴 🚵 🚵 🚵 🤸 🤸 🤸 🤼 🤼 🤼 🤽 🤽 🤽 🤾 🤾 🤾 🤹 🤹 🤹")
    #   person-resting
    st.write("🧘 🧘 🧘 🛀 🛌")
    #   family
    st.write("🧑 👭 👫 👬 💏 👩 👨 👩 💑 👩 👨 👩 👪 👨 👨 👨 👨 👨 👨 👨 👨 👨 👨 👩 👩 👩 👩 👩 👨 👨 👨 👨 👨 👩 👩 👩 👩 👩")
    #   person-symbol
    st.write("🗣 👤 👥 🫂 👣")
    # Component
    #   hair-style
    st.write("🦰 🦱 🦳 🦲")
    # Animals & Nature
    #   animal-mammal
    st.write("🐵 🐒 🦍 🦧 🐶 🐕 🦮 🐕 🐩 🐺 🦊 🦝 🐱 🐈 🐈 🦁 🐯 🐅 🐆 🐴 🫎 🫏 🐎 🦄 🦓 🦌 🦬 🐮 🐂 🐃 🐄 🐷 🐖 🐗 🐽 🐏 🐑 🐐 🐪 🐫 🦙 🦒 🐘 🦣 🦏 🦛 🐭 🐁 🐀 🐹 🐰 🐇 🐿 🦫 🦔 🦇 🐻 🐻 🐨 🐼 🦥 🦦 🦨 🦘 🦡 🐾")
    #   animal-bird
    st.write("🦃 🐔 🐓 🐣 🐤 🐥 🐦 🐧 🕊 🦅 🦆 🦢 🦉 🦤 🪶 🦩 🦚 🦜 🪽 🐦 🪿")
    #   animal-amphibian
    st.write("🐸")
    #   animal-reptile
    st.write("🐊 🐢 🦎 🐍 🐲 🐉 🦕 🦖")
    #   animal-marine
    st.write("🐳 🐋 🐬 🦭 🐟 🐠 🐡 🦈 🐙 🐚 🪸 🪼")
    #   animal-bug
    st.write("🐌 🦋 🐛 🐜 🐝 🪲 🐞 🦗 🪳 🕷 🕸 🦂 🦟 🪰 🪱 🦠")
    #   plant-flower
    st.write("💐 🌸 💮 🪷 🏵 🌹 🥀 🌺 🌻 🌼 🌷 🪻")
    #   plant-other
    st.write("🌱 🪴 🌲 🌳 🌴 🌵 🌾 🌿 ☘ 🍀 🍁 🍂 🍃 🪹 🪺 🍄")
    # Food & Drink
    #   food-fruit
    st.write("🍇 🍈 🍉 🍊 🍋 🍌 🍍 🥭 🍎 🍏 🍐 🍑 🍒 🍓 🫐 🥝 🍅 🫒 🥥")
    #   food-vegetable
    st.write("🥑 🍆 🥔 🥕 🌽 🌶 🫑 🥒 🥬 🥦 🧄 🧅 🥜 🫘 🌰 🫚 🫛")
    #   food-prepared
    st.write("🍞 🥐 🥖 🫓 🥨 🥯 🥞 🧇 🧀 🍖 🍗 🥩 🥓 🍔 🍟 🍕 🌭 🥪 🌮 🌯 🫔 🥙 🧆 🥚 🍳 🥘 🍲 🫕 🥣 🥗 🍿 🧈 🧂 🥫")
    #   food-asian
    st.write("🍱 🍘 🍙 🍚 🍛 🍜 🍝 🍠 🍢 🍣 🍤 🍥 🥮 🍡 🥟 🥠 🥡")
    #   food-marine
    st.write("🦀 🦞 🦐 🦑 🦪")
    #   food-sweet
    st.write("🍦 🍧 🍨 🍩 🍪 🎂 🍰 🧁 🥧 🍫 🍬 🍭 🍮 🍯")
    #   drink
    st.write("🍼 🥛 ☕ 🫖 🍵 🍶 🍾 🍷 🍸 🍹 🍺 🍻 🥂 🥃 🫗 🥤 🧋 🧃 🧉 🧊")
    #   dishware
    st.write("🥢 🍽 🍴 🥄 🔪 🫙 🏺")
    # Travel & Places
    #   place-map
    st.write("🌍 🌎 🌏 🌐 🗺 🗾 🧭")
    #   place-geographic
    st.write("🏔 ⛰ 🌋 🗻 🏕 🏖 🏜 🏝 🏞")
    #   place-building
    st.write("🏟 🏛 🏗 🧱 🪨 🪵 🛖 🏘 🏚 🏠 🏡 🏢 🏣 🏤 🏥 🏦 🏨 🏩 🏪 🏫 🏬 🏭 🏯 🏰 💒 🗼 🗽")
    #   place-religious
    st.write("⛪ 🕌 🛕 🕍 ⛩ 🕋")
    #   place-other
    st.write("⛲ ⛺ 🌁 🌃 🏙 🌄 🌅 🌆 🌇 🌉 ♨ 🎠 🛝 🎡 🎢 💈 🎪")
    #   transport-ground
    st.write("🚂 🚃 🚄 🚅 🚆 🚇 🚈 🚉 🚊 🚝 🚞 🚋 🚌 🚍 🚎 🚐 🚑 🚒 🚓 🚔 🚕 🚖 🚗 🚘 🚙 🛻 🚚 🚛 🚜 🏎 🏍 🛵 🦽 🦼 🛺 🚲 🛴 🛹 🛼 🚏 🛣 🛤 🛢 ⛽ 🛞 🚨 🚥 🚦 🛑 🚧")
    #   transport-water
    st.write("⚓ 🛟 ⛵ 🛶 🚤 🛳 ⛴ 🛥 🚢")
    #   transport-air
    st.write("✈ 🛩 🛫 🛬 🪂 💺 🚁 🚟 🚠 🚡 🛰 🚀 🛸")
    #   hotel
    st.write("🛎 🧳")
    #   time
    st.write("⌛ ⏳ ⌚ ⏰ ⏱ ⏲ 🕰 🕛 🕧 🕐 🕜 🕑 🕝 🕒 🕞 🕓 🕟 🕔 🕠 🕕 🕡 🕖 🕢 🕗 🕣 🕘 🕤 🕙 🕥 🕚 🕦")
    #   sky & weather
    st.write("🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘 🌙 🌚 🌛 🌜 🌡 ☀ 🌝 🌞 🪐 ⭐ 🌟 🌠 🌌 ☁ ⛅ ⛈ 🌤 🌥 🌦 🌧 🌨 🌩 🌪 🌫 🌬 🌀 🌈 🌂 ☂ ☔ ⛱ ⚡ ❄ ☃ ⛄ ☄ 🔥 💧 🌊")
    # Activities
    #   event
    st.write("🎃 🎄 🎆 🎇 🧨 ✨ 🎈 🎉 🎊 🎋 🎍 🎎 🎏 🎐 🎑 🧧 🎀 🎁 🎗 🎟 🎫")
    #   award-medal
    st.write("🎖 🏆 🏅 🥇 🥈 🥉")
    #   sport
    st.write("⚽ ⚾ 🥎 🏀 🏐 🏈 🏉 🎾 🥏 🎳 🏏 🏑 🏒 🥍 🏓 🏸 🥊 🥋 🥅 ⛳ ⛸ 🎣 🤿 🎽 🎿 🛷 🥌")
    #   game
    st.write("🎯 🪀 🪁 🔫 🎱 🔮 🪄 🎮 🕹 🎰 🎲 🧩 🧸 🪅 🪩 🪆 ♠ ♥ ♦ ♣ ♟ 🃏 🀄 🎴")
    #   arts & crafts
    st.write("🎭 🖼 🎨 🧵 🪡 🧶 🪢")
    # Objects
    #   clothing
    st.write("👓 🕶 🥽 🥼 🦺 👔 👕 👖 🧣 🧤 🧥 🧦 👗 👘 🥻 🩱 🩲 🩳 👙 👚 🪭 👛 👜 👝 🛍 🎒 🩴 👞 👟 🥾 🥿 👠 👡 🩰 👢 🪮 👑 👒 🎩 🎓 🧢 🪖 ⛑ 📿 💄 💍 💎")
    #   sound
    st.write("🔇 🔈 🔉 🔊 📢 📣 📯 🔔 🔕")
    #   music
    st.write("🎼 🎵 🎶 🎙 🎚 🎛 🎤 🎧 📻")
    #   musical-instrument
    st.write("🎷 🪗 🎸 🎹 🎺 🎻 🪕 🥁 🪘 🪇 🪈")
    #   phone
    st.write("📱 📲 ☎ 📞 📟 📠")
    #   computer
    st.write("🔋 🪫 🔌 💻 🖥 🖨 ⌨ 🖱 🖲 💽 💾 💿 📀 🧮")
    #   light & video
    st.write("🎥 🎞 📽 🎬 📺 📷 📸 📹 📼 🔍 🔎 🕯 💡 🔦 🏮 🪔")
    #   book-paper
    st.write("📔 📕 📖 📗 📘 📙 📚 📓 📒 📃 📜 📄 📰 🗞 📑 🔖 🏷")
    #   money
    st.write("💰 🪙 💴 💵 💶 💷 💸 💳 🧾 💹")
    #   mail
    st.write("✉ 📧 📨 📩 📤 📥 📦 📫 📪 📬 📭 📮 🗳")
    #   writing
    st.write("✏ ✒ 🖋 🖊 🖌 🖍 📝")
    #   office
    st.write("💼 📁 📂 🗂 📅 📆 🗒 🗓 📇 📈 📉 📊 📋 📌 📍 📎 🖇 📏 📐 ✂ 🗃 🗄 🗑")
    #   lock
    st.write("🔒 🔓 🔏 🔐 🔑 🗝")
    #   tool
    st.write("🔨 🪓 ⛏ ⚒ 🛠 🗡 ⚔ 💣 🪃 🏹 🛡 🪚 🔧 🪛 🔩 ⚙ 🗜 ⚖ 🦯 🔗 ⛓ 🪝 🧰 🧲 🪜")
    #   science
    st.write("⚗ 🧪 🧫 🧬 🔬 🔭 📡")
    #   medical
    st.write("💉 🩸 💊 🩹 🩼 🩺 🩻")
    #   household
    st.write("🚪 🛗 🪞 🪟 🛏 🛋 🪑 🚽 🪠 🚿 🛁 🪤 🪒 🧴 🧷 🧹 🧺 🧻 🪣 🧼 🫧 🪥 🧽 🧯 🛒")
    #   other-object
    st.write("🚬 ⚰ 🪦 ⚱ 🧿 🪬 🗿 🪧 🪪")
    # Symbols
    #   transport-sign
    st.write("🏧 🚮 🚰 ♿ 🚹 🚺 🚻 🚼 🚾 🛂 🛃 🛄 🛅")
    #   warning
    st.write("⚠ 🚸 ⛔ 🚫 🚳 🚭 🚯 🚱 🚷 📵 🔞 ☢ ☣")
    #   arrow
    st.write("⬆ ↗ ➡ ↘ ⬇ ↙ ⬅ ↖ ↕ ↔ ↩ ↪ ⤴ ⤵ 🔃 🔄 🔙 🔚 🔛 🔜 🔝")
    #   religion
    st.write("🛐 ⚛ 🕉 ✡ ☸ ☯ ✝ ☦ ☪ ☮ 🕎 🔯 🪯")
    #   zodiac
    st.write("♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓ ⛎")
    #   av-symbol
    st.write("🔀 🔁 🔂 ▶ ⏩ ⏭ ⏯ ◀ ⏪ ⏮ 🔼 ⏫ 🔽 ⏬ ⏸ ⏹ ⏺ ⏏ 🎦 🔅 🔆 📶 🛜 📳 📴")
    #   gender
    st.write("♀ ♂ ⚧")
    #   math
    st.write("✖ ➕ ➖ ➗ 🟰 ♾")
    #   punctuation
    st.write("‼ ⁉ ❓ ❔ ❕ ❗ 〰")
    #   currency
    st.write("💱 💲")
    #   other-symbol
    st.write("⚕ ♻ ⚜ 🔱 📛 🔰 ⭕ ✅ ☑ ✔ ❌ ❎ ➰ ➿ 〽 ✳ ✴ ❇ © ® ™")
    #   keycap
    st.write("# * 0 1 2 3 4 5 6 7 8 9 🔟")
    #   alphanum
    st.write("🔠 🔡 🔢 🔣 🔤 🅰 🆎 🅱 🆑 🆒 🆓 ℹ 🆔 Ⓜ 🆕 🆖 🅾 🆗 🅿 🆘 🆙 🆚 🈁 🈂 🈷 🈶 🈯 🉐 🈹 🈚 🈲 🉑 🈸 🈴 🈳 ㊗ ㊙ 🈺 🈵")
    #   geometric
    st.write("🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪ 🟥 🟧 🟨 🟩 🟦 🟪 🟫 ⬛ ⬜ ◼ ◻ ◾ ◽ ▪ ▫ 🔶 🔷 🔸 🔹 🔺 🔻 💠 🔘 🔳 🔲")
    # Flags
    #   flag
    st.write("🏁 🚩 🎌 🏴 🏳 🏳 🏳 🏴 ☠")


if __name__ == '__main__':
    main()
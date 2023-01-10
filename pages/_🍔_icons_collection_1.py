# Done by Muench
import streamlit as st


def main():
    st.set_page_config(page_title="icons_1", page_icon="🍔", layout="wide")

    sysmenu = '''
                  <style>
                  #MainMenu {visibility:hidden;}
                  footer {visibility:hidden;}
                  '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    st.subheader('Smileys & Emotion')
    st.text('face-smiling')
    '''😀 😃 😄 😁 😆 😅 🤣 😂 🙂 🙃 🫠 😉 😊 😇'''
    st.text("face-affection")
    '''🥰 😍 🤩 😘 😗 ☺ 😚 😙 🥲'''
    st.text("face-tongue")
    '''😋 😛 😜 🤪 😝 🤑'''
    st.text("face-hand")
    '''🤗 🤭 🫢 🫣 🤫 🤔 🫡'''
    st.text("face-neutral-skeptical")
    '''🤐 🤨 😐 😑 😶 🫥 😶 😏 😒 🙄 😬 😮 🤥 🫨'''
    st.text("face-sleepy")
    '''😌 😔 😪 🤤 😴'''
    st.text("face-unwell")
    '''😷 🤒 🤕 🤢 🤮 🤧 🥵 🥶 🥴 😵 😵 🤯'''
    st.text("face-hat")
    '''🤠 🥳 🥸'''
    st.text("face-glasses")
    '''😎 🤓 🧐'''
    st.text("face-concerned")
    '''😕 🫤 😟 🙁 ☹ 😮 😯 😲 😳 🥺 🥹 😦 😧 😨 😰 😥 😢 😭 😱 😖 😣 😞 😓 😩 😫 🥱'''
    st.text("face-negative")
    '''😤 😡 😠 🤬 😈 👿 💀 ☠'''
    st.text("face-costume")
    '''💩 🤡 👹 👺 👻 👽 👾 🤖'''
    st.text("cat-face")
    '''😺 😸 😹 😻 😼 😽 🙀 😿 😾'''
    st.text("monkey-face")
    '''🙈 🙉 🙊'''
    st.text("heart")
    '''💌 💘 💝 💖 💗 💓 💞 💕 💟 ❣ 💔 ❤ ❤ ❤ 🩷 🧡 💛 💚 💙 🩵 💜 🤎 🖤 🩶 🤍'''
    st.text("emotion")
    '''💋 💯 💢 💥 💫 💦 💨 🕳 💬 👁 🗨 🗯 💭 💤'''
    st.subheader("People & Body")
    st.text("hand-fingers-open")
    '''👋 🤚 🖐 ✋ 🖖 🫱 🫲 🫳 🫴 🫷 🫸'''
    st.text("hand-fingers-partial")
    '''👌 🤌 🤏 ✌ 🤞 🫰 🤟 🤘 🤙'''
    st.text("hand-single-finger")
    '''👈 👉 👆 🖕 👇 ☝ 🫵'''
    st.text("hand-fingers-closed")
    '''👍 👎 ✊ 👊 🤛 🤜'''
    st.text("hands")
    '''👏 🙌 🫶 👐 🤲 🤝 🙏'''
    st.text("hand-prop")
    '''✍ 💅 🤳'''
    st.text("body-parts")
    '''💪 🦾 🦿 🦵 🦶 👂 🦻 👃 🧠 🫀 🫁 🦷 🦴 👀 👁 👅 👄 🫦'''
    st.text("person")
    '''👶 🧒 👦 👧 🧑 👱 👨 🧔 🧔 🧔 👨 👨 👨 👨 👩 👩 🧑 👩 🧑 👩 🧑 👩 🧑 👱 👱 🧓 👴 👵'''
    st.text("person-gesture")
    '''🙍 🙍 🙍 🙎 🙎 🙎 🙅 🙅 🙅 🙆 🙆 🙆 💁 💁 💁 🙋 🙋 🙋 🧏 🧏 🧏 🙇 🙇 🙇 🤦 🤦 🤦 🤷 🤷 🤷'''
    st.text("person-role")
    '''🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 👮 👮 👮 🕵 🕵 🕵 💂 💂 💂 🥷 👷 👷 👷 🫅 🤴 👸 👳 👳 👳 👲 🧕 🤵 🤵 🤵 👰 👰 👰 🤰 🫃 🫄 🤱 👩 👨 🧑'''
    st.text("person-fantasy")
    '''👼 🎅 🤶 🧑 🦸 🦸 🦸 🦹 🦹 🦹 🧙 🧙 🧙 🧚 🧚 🧚 🧛 🧛 🧛 🧜 🧜 🧜 🧝 🧝 🧝 🧞 🧞 🧞 🧟 🧟 🧟 🧌'''
    st.text("person-activity")
    '''💆 💆 💆 💇 💇 💇 🚶 🚶 🚶 🧍 🧍 🧍 🧎 🧎 🧎 🧑 👨 👩 🧑 👨 👩 🧑 👨 👩 🏃 🏃 🏃 💃 🕺 🕴 👯 👯 👯 🧖 🧖 🧖 🧗 🧗 🧗'''
    st.text("person-sport")
    '''🤺 🏇 ⛷ 🏂 🏌 🏌 🏌 🏄 🏄 🏄 🚣 🚣 🚣 🏊 🏊 🏊 ⛹ ⛹ ⛹ 🏋 🏋 🏋 🚴 🚴 🚴 🚵 🚵 🚵 🤸 🤸 🤸 🤼 🤼 🤼 🤽 🤽 🤽 🤾 🤾 🤾 🤹 🤹 🤹'''
    st.text("person-resting")
    '''🧘 🧘 🧘 🛀 🛌'''
    st.text("family")
    '''🧑 👭 👫 👬 💏 👩 👨 👩 💑 👩 👨 👩 👪 👨 👨 👨 👨 👨 👨 👨 👨 👨 👨 👩 👩 👩 👩 👩 👨 👨 👨 👨 👨 👩 👩 👩 👩 👩'''
    st.text("person-symbol")
    '''🗣 👤 👥 🫂 👣'''
    st.subheader("Component")
    st.text("hair-style")
    '''🦰 🦱 🦳 🦲'''
    st.subheader("Animals & Nature")
    st.text("animal-mammal")
    '''🐵 🐒 🦍 🦧 🐶 🐕 🦮 🐕 🐩 🐺 🦊 🦝 🐱 🐈 🐈 🦁 🐯 🐅 🐆 🐴 🫎 🫏 🐎 🦄 🦓 🦌 🦬 🐮 🐂 🐃 🐄 🐷 🐖 🐗 🐽 🐏 🐑 🐐 🐪 🐫 🦙 🦒 🐘 🦣 🦏 🦛 🐭 🐁 🐀 🐹 🐰 🐇 🐿 🦫 🦔 🦇 🐻 🐻 🐨 🐼 🦥 🦦 🦨 🦘 🦡 🐾'''
    st.text("animal-bird")
    '''🦃 🐔 🐓 🐣 🐤 🐥 🐦 🐧 🕊 🦅 🦆 🦢 🦉 🦤 🪶 🦩 🦚 🦜 🪽 🐦 🪿'''
    st.text("animal-amphibian")
    '''🐸'''
    st.text("animal-reptile")
    '''🐊 🐢 🦎 🐍 🐲 🐉 🦕 🦖'''
    st.text("animal-marine")
    '''🐳 🐋 🐬 🦭 🐟 🐠 🐡 🦈 🐙 🐚 🪸 🪼'''
    st.text("animal-bug")
    '''🐌 🦋 🐛 🐜 🐝 🪲 🐞 🦗 🪳 🕷 🕸 🦂 🦟 🪰 🪱 🦠'''
    st.text("plant-flower")
    '''💐 🌸 💮 🪷 🏵 🌹 🥀 🌺 🌻 🌼 🌷 🪻'''
    st.text("plant-other")
    '''🌱 🪴 🌲 🌳 🌴 🌵 🌾 🌿 ☘ 🍀 🍁 🍂 🍃 🪹 🪺 🍄'''
    st.subheader("Food & Drink")
    st.text("food-fruit")
    '''🍇 🍈 🍉 🍊 🍋 🍌 🍍 🥭 🍎 🍏 🍐 🍑 🍒 🍓 🫐 🥝 🍅 🫒 🥥'''
    st.text("food-vegetable")
    '''🥑 🍆 🥔 🥕 🌽 🌶 🫑 🥒 🥬 🥦 🧄 🧅 🥜 🫘 🌰 🫚 🫛'''
    st.text("food-prepared")
    '''🍞 🥐 🥖 🫓 🥨 🥯 🥞 🧇 🧀 🍖 🍗 🥩 🥓 🍔 🍟 🍕 🌭 🥪 🌮 🌯 🫔 🥙 🧆 🥚 🍳 🥘 🍲 🫕 🥣 🥗 🍿 🧈 🧂 🥫'''
    st.text("food-asian")
    '''🍱 🍘 🍙 🍚 🍛 🍜 🍝 🍠 🍢 🍣 🍤 🍥 🥮 🍡 🥟 🥠 🥡'''
    st.text("food-marine")
    ''' 🦀 🦞 🦐 🦑 🦪'''
    st.text("food-sweet")
    '''🍦 🍧 🍨 🍩 🍪 🎂 🍰 🧁 🥧 🍫 🍬 🍭 🍮 🍯'''
    st.text("drink")
    '''🍼 🥛 ☕ 🫖 🍵 🍶 🍾 🍷 🍸 🍹 🍺 🍻 🥂 🥃 🫗 🥤 🧋 🧃 🧉 🧊'''
    st.text("dishware")
    '''🥢 🍽 🍴 🥄 🔪 🫙 🏺'''
    st.subheader("Travel & Places")
    st.text("place-map")
    '''🌍 🌎 🌏 🌐 🗺 🗾 🧭'''
    st.text("place-geographic")
    '''🏔 ⛰ 🌋 🗻 🏕 🏖 🏜 🏝 🏞'''
    st.text("place-building")
    '''🏟 🏛 🏗 🧱 🪨 🪵 🛖 🏘 🏚 🏠 🏡 🏢 🏣 🏤 🏥 🏦 🏨 🏩 🏪 🏫 🏬 🏭 🏯 🏰 💒 🗼 🗽'''
    st.text("place-religious")
    '''⛪ 🕌 🛕 🕍 ⛩ 🕋'''
    st.text("place-other")
    '''⛲ ⛺ 🌁 🌃 🏙 🌄 🌅 🌆 🌇 🌉 ♨ 🎠 🛝 🎡 🎢 💈 🎪'''
    st.text("transport-ground")
    '''🚂 🚃 🚄 🚅 🚆 🚇 🚈 🚉 🚊 🚝 🚞 🚋 🚌 🚍 🚎 🚐 🚑 🚒 🚓 🚔 🚕 🚖 🚗 🚘 🚙 🛻 🚚 🚛 🚜 🏎 🏍 🛵 🦽 🦼 🛺 🚲 🛴 🛹 🛼 🚏 🛣 🛤 🛢 ⛽ 🛞 🚨 🚥 🚦 🛑 🚧'''
    st.text("transport-water")
    '''⚓ 🛟 ⛵ 🛶 🚤 🛳 ⛴ 🛥 🚢'''
    st.text("transport-air")
    '''✈ 🛩 🛫 🛬 🪂 💺 🚁 🚟 🚠 🚡 🛰 🚀 🛸'''
    st.text("hotel")
    '''🛎 🧳'''
    st.text("time")
    '''⌛ ⏳ ⌚ ⏰ ⏱ ⏲ 🕰 🕛 🕧 🕐 🕜 🕑 🕝 🕒 🕞 🕓 🕟 🕔 🕠 🕕 🕡 🕖 🕢 🕗 🕣 🕘 🕤 🕙 🕥 🕚 🕦'''
    st.text("sky & weather")
    '''🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘 🌙 🌚 🌛 🌜 🌡 ☀ 🌝 🌞 🪐 ⭐ 🌟 🌠 🌌 ☁ ⛅ ⛈ 🌤 🌥 🌦 🌧 🌨 🌩 🌪 🌫 🌬 🌀 🌈 🌂 ☂ ☔ ⛱ ⚡ ❄ ☃ ⛄ ☄ 🔥 💧 🌊'''
    st.subheader("Activities")
    st.text("event")
    '''🎃 🎄 🎆 🎇 🧨 ✨ 🎈 🎉 🎊 🎋 🎍 🎎 🎏 🎐 🎑 🧧 🎀 🎁 🎗 🎟 🎫'''
    st.text("award-medal")
    '''🎖 🏆 🏅 🥇 🥈 🥉'''
    st.text("sport")
    '''⚽ ⚾ 🥎 🏀 🏐 🏈 🏉 🎾 🥏 🎳 🏏 🏑 🏒 🥍 🏓 🏸 🥊 🥋 🥅 ⛳ ⛸ 🎣 🤿 🎽 🎿 🛷 🥌'''
    st.text("game")
    '''🎯 🪀 🪁 🔫 🎱 🔮 🪄 🎮 🕹 🎰 🎲 🧩 🧸 🪅 🪩 🪆 ♠ ♥ ♦ ♣ ♟ 🃏 🀄 🎴'''
    st.text("arts & crafts")
    '''🎭 🖼 🎨 🧵 🪡 🧶 🪢'''
    st.subheader("Objects")
    st.text("clothing")
    '''👓 🕶 🥽 🥼 🦺 👔 👕 👖 🧣 🧤 🧥 🧦 👗 👘 🥻 🩱 🩲 🩳 👙 👚 🪭 👛 👜 👝 🛍 🎒 🩴 👞 👟 🥾 🥿 👠 👡 🩰 👢 🪮 👑 👒 🎩 🎓 🧢 🪖 ⛑ 📿 💄 💍 💎'''
    st.text("sound")
    '''🔇 🔈 🔉 🔊 📢 📣 📯 🔔 🔕'''
    st.text("music")
    '''🎼 🎵 🎶 🎙 🎚 🎛 🎤 🎧 📻'''
    st.text("musical-instrument")
    '''🎷 🪗 🎸 🎹 🎺 🎻 🪕 🥁 🪘 🪇 🪈'''
    st.text("phone")
    '''📱 📲 ☎ 📞 📟 📠'''
    st.text("computer")
    '''🔋 🪫 🔌 💻 🖥 🖨 ⌨ 🖱 🖲 💽 💾 💿 📀 🧮'''
    st.text("light & video")
    '''🎥 🎞 📽 🎬 📺 📷 📸 📹 📼 🔍 🔎 🕯 💡 🔦 🏮 🪔'''
    st.text("book-paper")
    '''📔 📕 📖 📗 📘 📙 📚 📓 📒 📃 📜 📄 📰 🗞 📑 🔖 🏷'''
    st.text("money")
    '''💰 🪙 💴 💵 💶 💷 💸 💳 🧾 💹'''
    st.text("mail")
    '''✉ 📧 📨 📩 📤 📥 📦 📫 📪 📬 📭 📮 🗳'''
    st.text("writing")
    '''✏ ✒ 🖋 🖊 🖌 🖍 📝'''
    st.text("office")
    '''💼 📁 📂 🗂 📅 📆 🗒 🗓 📇 📈 📉 📊 📋 📌 📍 📎 🖇 📏 📐 ✂ 🗃 🗄 🗑'''
    st.text("lock")
    '''🔒 🔓 🔏 🔐 🔑 🗝'''
    st.text("tool")
    '''🔨 🪓 ⛏ ⚒ 🛠 🗡 ⚔ 💣 🪃 🏹 🛡 🪚 🔧 🪛 🔩 ⚙ 🗜 ⚖ 🦯 🔗 ⛓ 🪝 🧰 🧲 🪜'''
    st.text("science")
    '''⚗ 🧪 🧫 🧬 🔬 🔭 📡'''
    st.text("medical")
    '''💉 🩸 💊 🩹 🩼 🩺 🩻'''
    st.text("household")
    '''🚪 🛗 🪞 🪟 🛏 🛋 🪑 🚽 🪠 🚿 🛁 🪤 🪒 🧴 🧷 🧹 🧺 🧻 🪣 🧼 🫧 🪥 🧽 🧯 🛒'''
    st.text("other-object")
    '''🚬 ⚰ 🪦 ⚱ 🧿 🪬 🗿 🪧 🪪'''
    st.subheader("Symbols")
    st.text("transport-sign")
    '''🏧 🚮 🚰 ♿ 🚹 🚺 🚻 🚼 🚾 🛂 🛃 🛄 🛅'''
    st.text("warning")
    '''⚠ 🚸 ⛔ 🚫 🚳 🚭 🚯 🚱 🚷 📵 🔞 ☢ ☣'''
    st.text("arrow")
    '''⬆ ↗ ➡ ↘ ⬇ ↙ ⬅ ↖ ↕ ↔ ↩ ↪ ⤴ ⤵ 🔃 🔄 🔙 🔚 🔛 🔜 🔝'''
    st.text("religion")
    '''🛐 ⚛ 🕉 ✡ ☸ ☯ ✝ ☦ ☪ ☮ 🕎 🔯 🪯'''
    st.text("zodiac")
    '''♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓ ⛎'''
    st.text("av-symbol")
    '''🔀 🔁 🔂 ▶ ⏩ ⏭ ⏯ ◀ ⏪ ⏮ 🔼 ⏫ 🔽 ⏬ ⏸ ⏹ ⏺ ⏏ 🎦 🔅 🔆 📶 🛜 📳 📴'''
    st.text("gender")
    '''♀ ♂ ⚧'''
    st.text("math")
    '''✖ ➕ ➖ ➗ 🟰 ♾'''
    st.text("punctuation")
    '''‼ ⁉ ❓ ❔ ❕ ❗ 〰'''
    st.text("currency")
    '''💱 💲'''
    st.text("other-symbol")
    '''⚕ ♻ ⚜ 🔱 📛 🔰 ⭕ ✅ ☑ ✔ ❌ ❎ ➰ ➿ 〽 ✳ ✴ ❇ © ® ™'''
    st.text("keycap")
    '''#️⃣ *️⃣ 0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟'''
    st.text("alphanum")
    '''🔠 🔡 🔢 🔣 🔤 🅰 🆎 🅱 🆑 🆒 🆓 ℹ 🆔 Ⓜ 🆕 🆖 🅾 🆗 🅿 🆘 🆙 🆚 🈁 🈂 🈷 🈶 🈯 🉐 🈹 🈚 🈲 🉑 🈸 🈴 🈳 ㊗ ㊙ 🈺 🈵'''
    st.text("geometric")
    '''🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪ 🟥 🟧 🟨 🟩 🟦 🟪 🟫 ⬛ ⬜ ◼ ◻ ◾ ◽ ▪ ▫ 🔶 🔷 🔸 🔹 🔺 🔻 💠 🔘 🔳 🔲'''
    st.subheader("Flags")
    st.text("flag")
    '''🏁 🚩 🎌 🏴 🏳 🏳 🏳 🏴 ☠'''


if __name__ == '__main__':
    main()

            murmur128.Reset();
            murmur128.Append("hello "u8.ToArray());
            murmur128.Append("world"u8.ToArray());
            buffer = murmur128.GetCurrentHash();
            Assert.AreEqual("e0a0632d4f51302c55e3b3e48d28795d", buffer.ToHexString());

            murmur128.Reset();
            murmur128.Append("hello worldhello world"u8.ToArray());
            buffer = murmur128.GetCurrentHash();
            Assert.AreEqual("76f870485d4e69f8302d4b3fad28fd39", buffer.ToHexString());

            murmur128.Reset();
            murmur128.Append("hello world"u8.ToArray());
            murmur128.Append("hello world"u8.ToArray());
            buffer = murmur128.GetCurrentHash();
            Assert.AreEqual("76f870485d4e69f8302d4b3fad28fd39", buffer.ToHexString());

            murmur128.Reset();
            murmur128.Append("hello worldhello "u8.ToArray());
            murmur128.Append("world"u8.ToArray());
            buffer = murmur128.GetCurrentHash();
            Assert.AreEqual("76f870485d4e69f8302d4b3fad28fd39", buffer.ToHexString());
        }

        [TestMethod]
        public void TestAppend()
        {
            var random = new Random();
            var buffer = new byte[random.Next(1, 2048)];
            random.NextBytes(buffer);
            for (int i = 0; i < 32; i++)
            {
                int split = random.Next(1, buffer.Length - 1);
                var murmur128 = new Murmur128(123u);
                murmur128.Append(buffer.AsSpan(0, split));
                murmur128.Append(buffer.AsSpan(split));
                Assert.AreEqual(murmur128.GetCurrentHash().ToHexString(), buffer.Murmur128(123u).ToHexString());
            }
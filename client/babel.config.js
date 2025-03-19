module.exports = function (api) {
  api.cache(true);
  return {
    presets: [
      ["babel-preset-expo", { jsxImportSource: "nativewind" }],
      "nativewind/babel",
    ],

    plugins: [
      ["module:react-native-dotenv"],
      [
        "module-resolver",
        {
          root: ["./src"],

          alias: {
            "@": "./src",
            "tailwind.config": "./tailwind.config.js",
          },
        },
      ],
    ],
  };
};

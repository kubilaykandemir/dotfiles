return {
  'williamboman/mason.nvim', -- Optional
  dependencies = {
    'williamboman/mason-lspconfig.nvim'
  }, -- Optional
  config = function()
    local mason = require("mason")

    local mason_lspconfig = require("mason-lspconfig")

    mason.setup({
      ui = {
        icons = {
          package_installed = "✓",
          package_pending = "➜",
          package_uninstalled = "✗"
        }
      }
    })

    mason_lspconfig.setup({
      ensure_installed = {
        "lua_ls",
        "rust_analyzer",
        "clangd",
        "tsserver",
        "cssls",
        "html",
        "tailwindcss",
        "emmet_ls",
        "bashls",
      },
      -- auto installs configured server with lspconfig
      automatic_installation = true,
    })
  end
}

return {
	"williamboman/mason.nvim", -- Optional
	dependencies = {
		"williamboman/mason-lspconfig.nvim",
		"WhoIsSethDaniel/mason-tool-installer.nvim",
	}, -- Optional
	config = function()
		local mason = require("mason")

		local mason_lspconfig = require("mason-lspconfig")

		local mason_tool_installer = require("mason-tool-installer")

		mason.setup({
			ui = {
				icons = {
					package_installed = "✓",
					package_pending = "➜",
					package_uninstalled = "✗",
				},
			},
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

		mason_tool_installer.setup({
			ensure_installed = {
				"prettier",
				"eslint_d",
				"stylua",
			},
		})
	end,
}

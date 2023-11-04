return {
	theme = "cattpuccin",
	"nvim-telescope/telescope-file-browser.nvim",
	dependencies = { "nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim" },
	config = function()
		-- You don't need to set any of these options.
		-- IMPORTANT!: this is only a showcase of how you can set default options!
		local telescope = require("telescope")
		local fb_actions = require("telescope._extensions.file_browser.actions")
		telescope.setup({
			extensions = {
				file_browser = {
					-- disables netrw and use telescope-file-browser in its place
					hijack_netrw = true,
					mappings = {
						["i"] = {
							-- your custom insert mode mappings
							["<A-c>"] = fb_actions.create,
							["<S-CR>"] = fb_actions.create_from_prompt,
							["<A-r>"] = fb_actions.rename,
							["<A-m>"] = fb_actions.move,
							["<A-y>"] = fb_actions.copy,
							["<A-d>"] = fb_actions.remove,
							["<C-o>"] = fb_actions.open,
							["<C-g>"] = fb_actions.goto_parent_dir,
							["<C-e>"] = fb_actions.goto_home_dir,
							["<C-w>"] = fb_actions.goto_cwd,
							["<C-t>"] = fb_actions.change_cwd,
							["<C-f>"] = fb_actions.toggle_browser,
							["<C-h>"] = fb_actions.toggle_hidden,
							["<C-s>"] = fb_actions.toggle_all,
							["<bs>"] = fb_actions.backspace,
						},
						["n"] = {
							-- your custom normal mode mappings
							["c"] = fb_actions.create,
							["r"] = fb_actions.rename,
							["m"] = fb_actions.move,
							["y"] = fb_actions.copy,
							["d"] = fb_actions.remove,
							["o"] = fb_actions.open,
							["g"] = fb_actions.goto_parent_dir,
							["e"] = fb_actions.goto_home_dir,
							["w"] = fb_actions.goto_cwd,
							["t"] = fb_actions.change_cwd,
							["f"] = fb_actions.toggle_browser,
							["h"] = fb_actions.toggle_hidden,
							["s"] = fb_actions.toggle_all,
						},
					},
				},
			},
		})

		telescope.load_extension("file_browser")

		vim.keymap.set(
			"n",
			"<space>fb",
			telescope.extensions.file_browser.file_browser,
			{ noremap = true, desc = "Telescope [F]ile [Browser]" }
		)
	end,
}

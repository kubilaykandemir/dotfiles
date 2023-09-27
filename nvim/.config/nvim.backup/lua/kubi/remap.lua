vim.g.mapleader = " "
vim.g.localmapleader= " "

vim.keymap.set("n", "<leader>pv", vim.cmd.Ex, { desc = "Vim File Explorer Netrw" })
-- Remap for dealing with word wrap
vim.keymap.set('n', 'k', "v:count == 0 ? 'gk' : 'k'", { expr = true, silent = true })
vim.keymap.set('n', 'j', "v:count == 0 ? 'gj' : 'j'", { expr = true, silent = true })

-- Remap fast jk press to ESC
vim.keymap.set('i', 'jk', '<ESC>', { desc = 'Remap fast jk press <ESC>' })

-- Diagnostic keymaps
vim.keymap.set('n', '[d', vim.diagnostic.goto_prev, { desc = 'Go to previous diagnostic message' })
vim.keymap.set('n', ']d', vim.diagnostic.goto_next, { desc = 'Go to next diagnostic message' })
vim.keymap.set('n', '<leader>e', vim.diagnostic.open_float, { desc = 'Open floating diagnostic message' })
vim.keymap.set('n', '<leader>q', vim.diagnostic.setloclist, { desc = 'Open diagnostics list' })

-- Move highlighted text with captial J and K up and down
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv", { desc = "Move highlighted text down" })
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv", { desc = "Move highlighted text up" })

-- For Os clipboard Leader Y and For Nvim clipboard Leader y
vim.keymap.set({ "n", "v" }, "<leader>y", [["+y]], { desc = "OS Clipboard" })
vim.keymap.set("n", "<leader>Y", [["+Y]], { desc = "OS Clipboard" })

vim.keymap.set("n", "<leader>s", "<leader>s", { desc = "[T]elescope Search "})
vim.keymap.set("n", "<leader>h", "<leader>h", { desc = "[H]arpoon" })
vim.keymap.set("n", "<leader>c", "<leader>c", { desc = "Lsp [C]ode Action" })

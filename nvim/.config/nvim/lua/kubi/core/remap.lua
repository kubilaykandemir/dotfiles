vim.g.mapleader = " "
vim.g.localmapleader = " "

vim.keymap.set("n", "<leader>pv", ":Lexplore<CR>", { desc = "Vim File Explorer Netrw" })
vim.keymap.set("n", "<leader>pw", ":Lexplore %:p:h<CR>", { desc = "Vim File Explorer Netrw" })

-- Remap for dealing with word wrap
vim.keymap.set("n", "k", "v:count == 0 ? 'gk' : 'k'", { expr = true, silent = true })
vim.keymap.set("n", "j", "v:count == 0 ? 'gj' : 'j'", { expr = true, silent = true })

-- Remap fast jk press to ESC
vim.keymap.set("i", "jk", "<ESC>", { desc = "Remap fast jk press <ESC>" })

-- Diagnostic keymaps
vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, { desc = "Go to previous diagnostic message" })
vim.keymap.set("n", "]d", vim.diagnostic.goto_next, { desc = "Go to next diagnostic message" })
vim.keymap.set("n", "<leader>e", vim.diagnostic.open_float, { desc = "Open floating diagnostic message" })
vim.keymap.set("n", "<leader>q", vim.diagnostic.setloclist, { desc = "Open diagnostics list" })

-- Move highlighted text with captial J and K up and down

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv", { desc = "Move highlighted text down" })
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv", { desc = "Move highlighted text up" })

-- For Os clipboard Leader Y and For Nvim clipboard Leader y
vim.keymap.set({ "n", "v" }, "<leader>y", [["+y]], { desc = "OS Clipboard" })
vim.keymap.set("n", "<leader>Y", [["+Y]], { desc = "OS Clipboard" })

vim.keymap.set("n", "]b", "<cmd>bnext<CR>", { desc = "Buffer Next" })
vim.keymap.set("n", "[b", "<cmd>bpre<CR>", { desc = "Buffer Previous" })
vim.keymap.set("n", "]B", "<cmd>blast<CR>", { desc = "Buffer Last" })
vim.keymap.set("n", "[B", "<cmd>bfirst<CR>", { desc = "Buffer First" })

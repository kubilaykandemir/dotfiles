return {
  -- Detect tabstop and shiftwidth automatically
  'tpope/vim-sleuth',

  -- Setup neovim lua configuration
  "folke/neodev.nvim",
  -- Useful status updates for LSP
  -- NOTE: `opts = {}` is the same as calling `require('fidget').setup({})`
  { 'j-hui/fidget.nvim', tag = 'legacy', opts = {} },

  "simrat39/rust-tools.nvim",
}

import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://wiki.letsbuilda.dev/',
	base: '/template',
	integrations: [
		starlight({
			title: 'TEMPLATE',
			editLink: {
				baseUrl: 'https://github.com/letsbuildawiki/template/edit/main/',
			},
			lastUpdated: true,
			social: {
				discord: 'https://discord.gg/hqPw9duXtP',
				github: 'https://github.com/letsbuildawiki/template',
			},
			sidebar: [
				{
					label: 'Home',
					link: '/'
				},
				// sidebar-items
			],
		}),
	],
});

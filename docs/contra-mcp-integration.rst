=====================================================
Contra Model Context Protocol (MCP) Integration Guide
=====================================================

:Author: René (Rénich) Bon Ćirić & Antigravity AI
:Date: 2026-09-19
:Endpoint: ``https://contra.com/mcp``
:Protocol: Model Context Protocol (Hosted Remote HTTP / SSE)

.. contents:: Table of Contents
   :depth: 2

Overview & Architecture
=======================

`Contra MCP <https://contra.com/features/mcp>`_ is Contra's official Model Context Protocol server. It exposes the entire Contra platform (messaging, hiring, proposals, invoicing, portfolio management, search) directly to AI assistants.

By connecting Contra MCP to our agentic engineering environment, we can operate your independent consulting practice directly from conversation—eliminating manual browser tab hopping for client communications, proposal dispatch, and invoice generation.

Endpoint & Authentication Specifications
========================================

* **Server URL**: ``https://contra.com/mcp``
* **Transport**: Remote Hosted Streamable HTTP / Server-Sent Events (SSE)
* **Auth Protocol**: OAuth 2.0 Protected Resource (Bearer token)
* **Resource Metadata**: ``https://contra.com/.well-known/oauth-protected-resource/mcp``
* **Authorization Server**: ``https://contra.com/api``
* **Scopes Supported**: ``mcp:tools``

Core Capabilities (60+ Platform Tools)
======================================

1. Dealflow & Proposals
-----------------------

* Generate and dispatch modular fixed-price or milestone proposals.
* Convert client briefs into structured scopes of work.
* Submit custom project bids directly into active client inquiries.

2. Client Communication & Monitoring
------------------------------------

* Inspect unread client messages and project notifications.
* Draft context-aware responses to inbound leads.
* Review contract state, escrow funding status, and milestone approvals.

3. Invoicing & Cashflow Operations
----------------------------------

* Generate commission-free invoices for completed milestones.
* Generate instant one-click payment links for discovery audits.
* Track payment statuses, dispute resolution, and bank payouts.

4. Portfolio & Service Synchronization
--------------------------------------

* Publish new productized services directly to your public profile.
* Update case study copy, metrics, and project assets programmatically.
* Sync digital products or specialized tooling subscriptions.

Safety & Governance: The Prepare-and-Confirm Flow
=================================================

Contra MCP implements an explicit two-step **Prepare-and-Confirm** safety model for all state-mutating operations:

#. **Draft & Preview**: The AI prepares a proposed action (e.g. sending a $5,000 proposal or dispatching a message) and presents a complete preview.
#. **Explicit Approval**: Nothing is committed or visible to the client until you explicitly approve the action.
#. **Auto-Expiration**: If a prepared action is not confirmed within 15 minutes, it is automatically discarded.

Client Integration Recipes
==========================

Claude Code (CLI)
-----------------

To connect Contra MCP in Claude Code, execute:

.. code-block:: bash

   claude mcp add contra https://contra.com/mcp

Cursor & Windsurf
-----------------

Add the server configuration to ``~/.cursor/mcp.json`` or ``mcp_config.json``:

.. code-block:: json

   {
     "mcpServers": {
       "contra": {
         "serverUrl": "https://contra.com/mcp"
       }
     }
   }

Antigravity / Gemini CLI Configuration
--------------------------------------

Configure the remote SSE endpoint within your Antigravity MCP settings:

.. code-block:: json

   {
     "mcpServers": {
       "contra": {
         "url": "https://contra.com/mcp",
         "type": "sse",
         "headers": {
           "Authorization": "Bearer YOUR_CONTRA_TOKEN"
         }
       }
     }
   }

Partnership Workflow with Contra MCP
====================================

Once authenticated, our daily operations streamline into conversational commands:

* *"Gemini, poll Contra for unread client inquiries."*
* *"Gemini, review this inbound inquiry, run it through our intake rubric, and draft an SOW proposal."*
* *"Gemini, generate an invoice on Contra for Acme Milestone 1 and create a payment link."*
